# Auto-GPT: 基于Auto-GPT的交互式AI命令-中文翻译版

编写目的：Auto-GPT在执行和返回命令时，通常会输出一大段英文，且返回内容不可预期，提前翻译会提高很多交互效率。（每次都得打开翻译软件粘贴的我，觉得这样很蠢）

## 💾 如何使用
### 获取翻译api-key
翻译使用baidu-api进行翻译，需要您先获取到翻译的APP ID，和秘钥：
http://api.fanyi.baidu.com/api/trans/product/desktop

在此页面可以找到APP ID和秘钥：
http://api.fanyi.baidu.com/manage/developer

使用方式同Auto-GPT，在启动脚本之前，需要添加环境变量
对于 linux 或者 Mac OS用户
```
export TRANSLATE_API_NAME="baidu"
export TRANSLATE_API_ID="你的APP ID"
export TRANSLATE_API_KEY="你的秘钥"
```

对于 Windows 用户：
```
setx TRANSLATE_API_NAME "baidu"
setx TRANSLATE_API_ID "你的APP ID"
setx TRANSLATE_API_KEY "你的秘钥"
```

## 注意⚠️
百度免费的翻译API，
标准版：QPS=1,免费调用量5万字符/月
高级版：QPS=10,免费调用量100万字符/月
若每月调用量超过免费调用量限制，将按照49元/百万字符进行计费；

普通个人用户可以免费升级高级版

## 🔍效果

### 示例：启动
<image src="https://github.com/anignx/Auto-GPT-Translate/blob/master/2023-04-16_01.30.54.png?raw=true">

### 示例：任务 & 执行
<image src="https://github.com/anignx/Auto-GPT-Translate/blob/master/2023-04-16_01.31.45.png?raw=true">

### 示例：任务 & 执行
<image src="https://github.com/anignx/Auto-GPT-Translate/blob/master/2023-04-16_01.32.36.png?raw=true">

## 警告⚠️
目前Auto-GPT迭代速度很快，几乎每天代码都不一样，只有master分支，没有release版本，并且存在各种bug。
Auto-GPT可能会在用户授权后执行任何命令，其中包括：
```
自行编写并执行python脚本，调用浏览器阅读，创建本地文件。
```
为了防止非预期情况，请尽量在虚拟机环境下运行；或者请仔细阅读AI反馈的`下一步要执行的命令`

## 交流群
<image src="https://github.com/anignx/Auto-GPT-Translate/blob/master/IMG_9950.jpg?raw=true">
