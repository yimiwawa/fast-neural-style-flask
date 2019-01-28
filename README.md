# 图片风格快速转换的简单web实现

本项目核心代码基于[fast-neural-style-tensorflow](https://github.com/hzy46/fast-neural-style-tensorflow)，在此基础上，添加了简单的flask框架，实现了页面上传图片，选择转换风格，生成转换图片并展示的流程。

## Requirements：
- Python 2.7.x
- <b>Now support Tensorflow >= 1.0</b>
- pyyaml
- flask
- gevent

## 训练模型
在原项目带有的7中模型（wave，cubist，denoised_starry，mosaic，scream，feathers，udnie）基础上，添加了铅笔画的模型[pencil]().


## 部署与运行:

web服务端代码位于predict_flask.py文件中，修改代码中host、port，执行

```
python predict_flask.py
```
即可启动服务。

在浏览器中输入 http://host:port/index，即可用。

## 示例
| configuration | style | sample |
| :---: | :----: | :----: |
| [pencil.yml](https://github.com/hzy46/fast-neural-style-tensorflow/blob/master/conf/wave.yml) |![](https://github.com/hzy46/fast-neural-style-tensorflow/blob/master/img/results/style_wave.jpg)|  ![](https://github.com/hzy46/fast-neural-style-tensorflow/blob/master/img/results/wave.jpg)  |


