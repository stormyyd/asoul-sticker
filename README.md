# A-SOUL Sticker

这是一个存储了A-SOUL B站装扮表情包的仓库，同时包含了一个css文件，你可以将其引入您的网站，这样就可以像这样使用这些可爱的表情包了：

```html
<p style="font-size: 32px;">
  我们是：
  <span class="ava_asoul"></span>
  <span class="bella_asoul"></span>
  <span class="carol_asoul"></span>
  <span class="diana_asoul"></span>
  <span class="eileen_asoul"></span>
</p>
```

[在线演示](https://codepen.io/stormyyd/pen/jOaJMbx)

欢迎关注：

- [@向晚大魔王](https://space.bilibili.com/672346917)
- [@贝拉kira](https://space.bilibili.com/672353429)
- [@珈乐Carol](https://space.bilibili.com/351609538)
- [@嘉然今天吃什么](https://space.bilibili.com/672328094)
- [@乃琳Queen](https://space.bilibili.com/672342685)
- ~~[@A-SOUL_Official](https://space.bilibili.com/703007996)~~ 这个可以不关注

## Usage

```html
<!--引入CSS-->
<link rel="stylesheet" href="//cdn.jsdelivr.net/gh/stormyyd/asoul-sticker/dist/asoul-sticker.css">

<!--使用span标签，将类名设置为表情包名称即可-->
<span class="diana_asoul"></span>
```

目前查表情包名字只能自己去`asset`文件夹里翻，之后会做一个网站来查询的，别急。

## 自定义配置

### CSS

你可以通过修改`config.json`文件后，运行`main.py`来生成自己定制化的css，目前只做了两个配置项：

```json5
{
    // 如果你有自己的服务器，可以将仓库的asset文件夹上传到你自己的服务器，
    // 同时修改该参数，即可使用你自己的服务器来加载表情包了。注意该参数的末尾一定要有"/"，
    // 比较懒狗，没对末尾的斜杠做处理。
    "host": "cdn.jsdelivr.net/gh/stormyyd/asoul-sticker/asset/", 
    // 高度参数，默认为2em，即两倍父元素的font-size大小，如果有需要可以自行修改。
    "height": "2em"
}
```

### data.txt

该文件存储了表情包的元数据，格式定义为：

- "\#" 符号开头的为注释行，不参与处理
- 行首和行尾的所有空格符号均会被忽略（具体取决于Python `str.strip()` 函数的实现）
- 一行表示一个表情包
- 一行数据有四列，每列数据使用**一个**空格（" "，ASCII 32）分割
- 第一列表示表情包所在的子文件夹
- 第二列表示表情包的文件名
- 第三列表示该表情包在css中的类名
- 第四列表示该表情包的名称，基本来自B站，部分名字因为太过于鬼屎，个人做了一些小修改，跟B站的不完全相同。该列数据目前其实也不参与处理，本来是准备将其作为`img`标签的`alt`属性的值的，但目前这个实现压根没用到`img`标签
- 每列数据均不能包含空格，也不支持转义，建议使用下划线（"_"，ASCII 95）替代

## TODO

- [ ] 一个查询表情包class取值的网站
- [ ] 加入微信表情包
