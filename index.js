(() => {
  'use strict'
  let clipboard = new ClipboardJS('.btn-copy')
  let notyf = new Notyf({
    position: {
      x: 'center',
      y: 'top',
    },
  })
  clipboard.on('success', e => {
    console.log(e)
    notyf.success('已复制到剪贴板')
  })
  clipboard.on('error', e => {
    console.log(e)
    notyf.error('复制失败')
  })
  addBackToTop({
    diameter: 56,
    backgroundColor: '#FC966E',
    textColor: '#fff'
  })
})()
