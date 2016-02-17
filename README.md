# Wechat Image Conversion

## 注意

1. 需要使用Python运行,且需要binascii包,推荐装一个winPython或是anaconda

2. 不要外传,以免算法失效

## 使用指南

### 查找dat文件

电脑端的话...打开文件夹:

我的文档\WeChat Files\你的用户名\Data

然后通过两种方法查找原始的dat文件:

1. 根据修改时间

2. 在电脑端的微信上找到那张图片的前后图片,
然后右键保存,从弹出的保存窗口中复制默认的文件名,
然后在文件夹中搜索文件名,会找到一个和此保存的文件名相似的dat文件,
然后查找前后.

### 操作步骤

1. 通过在电脑端发送color_sheet.jpg文件,得到dat文件,
复制到代码文件夹,更名为color_trans.dat

2. 把需要转换的文件复制进代码文件夹,更名为in.dat

3. 运行代码:python wic.py

4. 查看out.jpg文件

如果觉得能用,[知乎](https://www.zhihu.com/question/35056157/answer/85231763)点个赞吧...