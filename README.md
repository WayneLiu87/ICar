# ICar

自动控制小车项目计划：

第一阶段（2015.4）：

	硬件平台组建：4驱小车，树莓派，摄象头，音响，麦克风,无线网卡	DONE
	语音识别和tts：调用一些免费的API，实现听说功能 DONE
	简单视频图像处理：获取摄象头中的图片，使用开源图像识别工具，做一些简单的识别 （opencv暂时不能安装，再想其他方案)
	爬虫：可以下载网页(done)，并解析文本，分词，分句 TODO(bs4 jieba)
	网页播放：用爬虫下载网页，并且说出网页中的文本 TODO
	小车控制：简单的方向控制（前，后，左，右，变速）DONE，自定义路线驾驶（直线 DONE，转圈 TODO） 
	

第二阶段（2016.08-2016.12)：

	硬件平台扩展：超声波模块，二自由度云台
	语音识别，TTS，图像识别，能够构建自己的系统（开源工具），而不是调用第三方的API（解决速度慢的问题）
		拟用juliusjs/cmusphinx做语音识别，ekko做TTS	
	小车控制：用超声波测距来避障（条件反射系统）
	用神经网络做控制器
	

第三阶段：（2016.12-）

	自然语言理解:
		文本情感分类：参考：https://github.com/dennybritz/cnn-text-classification-tf
	知识库，简单推理
		做知识库的入门知识，希望能有这方面经验的人提供些资料
	语音识别，图像识别（state of art成果研究，尝试实现。）
	对话系统：简单问答
	

