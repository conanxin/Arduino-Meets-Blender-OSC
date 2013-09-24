Arduino-Meets-Blender-OSC
=========================

###Arduino通过Processing使用OSC协议来控制Blender

###来自Google Code上的[chrisworld-projects](https://code.google.com/p/chrisworld-projects/wiki/ArduinoMeetsBlender)

这个项目展示了如何使用Ardunio通过OSC协议在Blenders Game Engine中控制对象。它最初是用来创建实时的digital puppetry。

但是它能用来作为任何项目需要通过OSC（Open Sound Control）协议来和Blender的GameEngine通信的例子。

由于这个项目中使用的是OSC协议，那么任何能使用OSC的应用都可以发送数据给Blender　GameEngine.


----------
 
####要求：
[oscP5 library](http://www.sojamo.de/libraries/oscP5/index.html)

[Python SimpleOSC ](http://www.ixi-audio.net/content/body_backyard_python.html)

SimpleOSC是一个简单的API用于Python的Open Sound Control。
同样的，你还需要Arduino IDE, Processing IDE和Blender来完成这个项目。
你还需要一个Arduino板，线以及一个电位计。

--------- 
##过程

###1.硬件：
基本上你需要一个Arduino、三针的电位计，线，来完成这个demo。电位计的中针连接Arduino的Analog 3输入端口。其它两针连接5 Volt和GND。
从这个针读到的值的范围是：( 0 to 1023, 0 to 5 Volts)
找到Arduino连接的串口，在我的电脑上是COM4。然后就可以将Arduino的代码编译上传到Arduino板上了。
 
###2.Processing：
你需要在Processing中安装oscP5（http://www.sojamo.de/oscP5）， 将oscP5文件夹放在目录“processing-2.0.3\modes\java\libraries“下。之后确保你能**import oscP5***。
 
其中要改变oscarduino.pde文件中的String portname = "COM4"为你的串口号，注意变量TO_PORT和FROM_PORT。Blender中的脚本要监听一个PORT。这个PORT应该对应于processing文件中TO_PORT变量。
 
你也需要改变HOST变量对应于你的localhost（PC上为127.0.0.1）。
 
###3.Blender:
这个例子是在Blender 2.49b下完成的。要确保脚本arduino_to_blender.py已经加载到Blender中。在这个脚本你需要使PORT对应于processing中的TO_PORT。
 
在这里我已经为Python安装了OSC module，可以在python中试一下"**import OSC**"是否成功。
 
你需要注意arduino_to_blender.py脚本中：

*#检查下防火墙没有挡住这个端口 

*#这个端口要对应Processing 发送OSC信息的端口*
PORT = 2014  # ;) 
 
*#要设置和localhost相同的地址
HOST = "127.0.0.1"
 
其中直接在Blender下运行这个脚本是不行的，需要在Blender Game Engine下才能运行。
 
###4.测试运行：
一旦完成了所有步骤，你可以运行processing，在Blender下按P键在GameEngine下运行Blender。
转动电位计，然后你会看到Blender中的仪表盘运动。
 
###注意：
如果测试不工作，使用更高的端口数。要保证防火墙没有挡住端口。同样的要检测HOST和你的localhost IP相同。
 
***processing下有一个测试模式，来避免在Arduino处会出现问题。设置"TEST = true"，如果你要测试向Blender中发送数据，你可以在processing的面板中移动你的鼠标。***
