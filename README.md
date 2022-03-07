# A-SOUL Sticker

这是一个存储了A-SOUL官方表情包的仓库。

目前包含了以下表情：

- 五位成员的一期B站装扮表情
- 五位成员的官方抖音/微信表情
- 阿草的两套官方抖音/微信表情 ~~我一直是草学长啊~~
- 嘉然的B站舰长表情

该仓库同时包含了一个css文件，你可以将其引入您的网站，这样就可以像这样使用这些可爱的表情包了：

```html
<p style="font-size: 32px;">
  我们是：
  <span class="diana_asoul"></span>
  <span class="ava_asoul"></span>
  <span class="eileen_asoul"></span>
  <span class="carol_asoul"></span>
  <span class="bella_asoul"></span>
</p>
```

[Codepen 在线演示](https://codepen.io/stormyyd/pen/jOaJMbx) | [全表情包在线展示与查询](https://stormyyd.github.io/asoul-sticker/) | [自行部署效果演示](https://stormyyd.com/a-soul-sticker/)

欢迎关注：

- [@向晚大魔王](https://space.bilibili.com/672346917)
- [@贝拉kira](https://space.bilibili.com/672353429)
- [@珈乐Carol](https://space.bilibili.com/351609538)
- [@嘉然今天吃什么](https://space.bilibili.com/672328094)
- [@乃琳Queen](https://space.bilibili.com/672342685)
- ~~[@A-SOUL_Official](https://space.bilibili.com/703007996)~~ 这个可以不关注


## 声明

该项目为粉丝自制项目，一切与项目相关的行为均为粉丝行为，与 A-SOUL制作委员会 无任何关系。

请通过以下渠道关注官方消息：

- [Bilibili @A-SOUL_Official](https://space.bilibili.com/703007996)
- [新浪微博 @A-SOUL_Official](https://weibo.com/u/7519401668)
- [抖音 @五个魂儿呀](https://www.douyin.com/user/MS4wLjABAAAAflgvVQ5O1K4RfgUu3k0A2erAZSK7RsdiqPAvxcObn93x2vk4SKk1eUb6l_D4MX-n)（抖音号：ASOULofficial）

## Usage

当前版本：0.2.1

```html
<!--引入CSS-->
<link rel="stylesheet" href="https//cdn.jsdelivr.net/gh/stormyyd/asoul-sticker@0.2/dist/asoul-sticker.css">

<!--使用span标签，将类名设置为表情包名称即可-->
<span class="diana_asoul"></span>
```

你可以通过前往[这里](https://stormyyd.github.io/asoul-sticker/)查询表情包的class取值或直接复制表情包的代码来进行使用。

## 自定义配置

### CSS

你可以通过修改`config.json`文件后，运行`main.py`来生成自己定制化的css，目前只做了三个配置项：

```json5
{
    // 如果你有自己的服务器，可以将仓库的asset文件夹上传到你自己的服务器，
    // 同时修改该参数，即可使用你自己的服务器来加载表情包了。
    "host": "https://cdn.jsdelivr.net/gh/stormyyd/asoul-sticker@0.2/asset", 
    // 高度参数，默认为3em，即三倍父元素的font-size大小，如果有需要可以自行修改。
    "height": "3em",
    // 如果你希望将asset文件夹中的所有表情包打平为一层，即不需要使用子文件夹来区分不同人的表情包，
    // 则可以将该参数设为true
    "flatten": false
}
```

### data.txt

该文件存储了表情包的元数据，格式定义为：

- "\#" 符号开头的为注释行，不参与处理
- 行首和行尾的所有空格符号均会被忽略（具体取决于Python `str.strip()` 函数的实现）
- 一行表示一个表情包
- 一行数据有四列，每列数据使用**一个**空格（" "，ASCII 32）分割
- 第一列表示表情包所在的子文件夹，如果`flatten`参数为`true`，该值会被忽略
- 第二列表示表情包的文件名
- 第三列表示该表情包在css中的类名
- 第四列表示该表情包的名称，基本来自B站，部分名字因为太过于鬼屎，个人做了一些小修改，跟B站的不完全相同。如果浏览器不支持[Element replacement](https://developer.mozilla.org/en-US/docs/Web/CSS/content#element_replacement)，该列的文字会出现在使用表情包的地方，类似：`[嘉然_我们是A-SOUL]`
- 每列数据均不能包含空格，也不支持转义，建议使用下划线（"_"，ASCII 95）替代

## TODO

- [ ] 一个基于`JavaScript`的、可以在线生成客制化CSS的网站
