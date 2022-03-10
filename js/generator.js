'use strict';

(() => {
  let cssTemplate = null
  let stickerTemplate = null
  let stickerMetaData = null

  const notyf = new Notyf({
    position: {
      x: 'center',
      y: 'top',
    },
  })
  const clipboard = new ClipboardJS('.copy-btn')
  clipboard.on('success', e => {
    console.log(e)
    e.clearSelection()
    notyf.success('已复制到剪贴板')
  })
  clipboard.on('error', e => {
    console.log(e)
    notyf.error('复制失败')
  })

  function generateCSS({versionTag, host, height, flatten}) {
    host = host.replace(/\/+$/g, '') // trimRight('/')
    
    const tasks = []
    if (cssTemplate === null) {
      const task = fetch(`https://cdn.jsdelivr.net/gh/stormyyd/asoul-sticker@${versionTag}/asoul-sticker-base.css`)
        .then(response => response.text())
        .then(text => cssTemplate = text)
      tasks.push(task)
    }
    if (stickerTemplate === null) {
      const task = fetch(`https://cdn.jsdelivr.net/gh/stormyyd/asoul-sticker@${versionTag}/asoul-sticker-template.css`)
      .then(response => response.text())
      .then(text => stickerTemplate = text)
      tasks.push(task)
    }
    if (stickerMetaData === null) {
      const task = fetch(`https://cdn.jsdelivr.net/gh/stormyyd/asoul-sticker@${versionTag}/data.txt`)
      .then(response => response.text())
      .then(text => {
        stickerMetaData = text
          .split('\n')
          .map(line => line.trim())
          .filter(line => line.length > 0 && line[0] != '#')
          .map(line => line.split(' '))
      })
      tasks.push(task)
    }

    return Promise
      .all(tasks)
      .then(() => {
        const stickers = stickerMetaData
          .map(item => {
            const [dirName, fileName, className, alterName] = item
            const stickerHost = flatten ? host : `${host}/${dirName}`
            return stickerTemplate
              .replace(/\$className/g, className)
              .replace(/\$host/g, stickerHost)
              .replace(/\$filename/g, fileName)
              .replace(/\$alt/g, `[${alterName}]`)
          })
          .join('')

        const selectors = Array
          .from(new Set(stickerMetaData.map(item => item[0])))
          .sort()
          .map(prefix => `span[class^="${prefix}_"]`)
          .join(',\n')
        const cssBase = cssTemplate
          .replace(/\$version/g, versionTag)
          .replace(/\$host/g, host)
          .replace(/\$height/g, height)
          .replace(/\$flatten/g, flatten.toString())
          .replace(/\$selectors/g, selectors)

        return cssBase + '\n' + stickers
      })
  }

  document
    .getElementById('generate-btn')
    .addEventListener('click', () => {
      generateCSS({
        versionTag: document.getElementById('input-tag').value,
        host: document.getElementById('input-host').value,
        height: document.getElementById('input-height').value,
        flatten: document.getElementById('input-flatten').checked,
      })
      .then(css => {
        document.getElementById('generated-css').value = css
      })
      .catch((e) => {
        console.error('fetch template failed', e)
        notyf.error('获取模板文件失败，请检查网络连接')
      })
    })
  
  document
    .getElementById('clear-cache-btn')
    .addEventListener('click', () => {
      cssTemplate = null
      stickerTemplate = null
      stickerMetaData = null
      notyf.success('数据缓存已清除')
    })

  document.getElementById('generate-btn').click()
})()
