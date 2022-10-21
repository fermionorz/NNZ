# NNZ

> 重保的告警数量还可以，写写工具，看看S12全球总决赛，慢慢长夜很快就过去了。

## 简介

一款模块化工具，可以为命令行工具提供通用GUI界面。让你拥有自己喜欢的工具包。不论是在虚拟机里！还是装在U盘里！都可即插即用！

技术栈：Python + tkinter + toml

[+] 功能完善后再开源

另外，作为一个Linuxer，我还是很喜欢终端界面的🤭

### 三个好处

1. 好心情：在肾透厕视或者攻防演练的时候，打开各种终端窗口，然后整个电脑乱的一批，很让人烦躁，NNZ可以减轻你在这方面的痛苦。

2. 好简单：对于小白来说，很多工具不会用，不好学，有了前辈写好的配置文件，拿来可以直接梭哈了。

3. 好方便：有一天你不小心运行了一个exe，发现中招了，这个时候电脑不干净了，你左思右想还是选择了重装系统，TA可以让你一小时恢复工作状态。

## 主要功能

* 启动器 (把其他有GUI界面的工具集成一下) ~随便加了几个工具，没别的意思~

![image](assets/image-20221022020506-xs0o2m5.png)

​

* 渗透小工具 (现在还什么都没有，牛奶会有的，面包也会有的)

![image](assets/image-20221022020601-vhqqmcd.png)

​

* 命令行工具 (通用GUI界面，只需要写一份极其简单的配置文件即可，摆脱了在命令行里面切换各种目录的繁琐。)

![image](assets/image-20221022020711-h6vc09a.png)​

目前可以用exe：

- nzz_beta.7z       # 无任何第三方exe

- nzz_beta_demo.7z  # 仅配置文件


### nzz.exe hash校验

```
PS C:\> certutil -hashfile nnz.exe [md5, SHA1, SHA256]
MD5 的 dist/nnz.exe 哈希:
8396f27b74a5af53baf58d46e78675c9
SHA1 的 dist/nnz.exe 哈希:
5b3333889f742b67aee9f35ac0b6b459547db67d
SHA256 的 dist/nnz.exe 哈希:
d5673d6ac5b7c2e4f19ce3bc3b760057bbad78744f24a2fbbca17b395060b7cb
```

## 目录与使用说明

> 加粗部分比较重要。

**NNZ/**

* NNZ.exe
* res/

  * env/

    * python3/

      * python.exe
    * java8/

      * bin/

        * java.exe
        * javaw.exe
    * **env.toml**
  * images/

    * logo.png
    * icon.png
  * runs/

    * BurpSuite/

      * BurpSuite.bat
      * BurpSuite.png
    * */
  * **SecLists/**
  * **simple_tools/**
  * **terminal_tools/**

    * dirsearch/

      * dirsearch.py
      * dirsearch.toml
      * *
    * fscan/

      * fscan.exe
      * fscan.toml
    * gobuster dir/

      * gobuster.exe
      * gobuster dir.toml
    * gobuster dns/

      * gobuster.exe
      * gobuster dns.toml

### 详细介绍

* NNZ/res/env/toml

```Config.toml
# 用于记载便携式环境的位置,主要为terminal_tools提供索引, 终端工具中有一些时exe文件，所以加个None=''表示父进程为空。
# 此文件必须存在
java8 = "res/env/jdk8/bin/java.exe"
java11 = "res/env/jdk11/bin/java.exe"
python2 = "res/env/python2/python.exe"
python3 = "res/env/python3/python.exe"
None = ''
```

* NNZ/res/runs/BurpSuite/

```
# 拿BurpSuite举个栗子
NNZ/res/runs/BurpSuite/BurpSuite.bat
NNZ/res/runs/BurpSuite/BurpSuite.png
NNZ/res/runs/BurpSuite/BurpSuite.jar

# 添加启动器的方法很简单：
	1.在NNZ/res/runs/ 目录下面新建文件夹: [name]/；
	2.在该文件夹下创建同名: [name].bat 文件；
	3.在文件夹下添加图标文件 [name].png 必须是png格式；
	4.编写bat文件，确保双击bat文件可以运行工具。
BurpSuite.bat
-------------
cd /d %~dp0
start /B javaw.exe -Xmx8G -XX:-UseParallelGC -noverify -javaagent:BurpSuiteLoader.jar -Dfile.encoding=utf-8 -jar BurpSuite.jar
-------------
# 这里用javaw.exe运行，可以自动创建新进程，与NNZ.exe进程分离，直接把工具的java.exe换成javaw.exe就行，Python对应的也有pythonw.exe。

# 同时也可以用于启动.jar .py .exe ..... 各种类型的程序，只要双击bat能运行就可。

# exe类型可以用下面的这种格式
Clash.bat
----------
cd /d %~dp0
start /b "Clash" "Clash for Windows.exe"
----------

# 环境也可以用自己添加的环境，这样方便构建自己的工具包
Godzilla.bat
----------
cd /d %~dp0
Start /b ../../env/jdk11/bin/javaw.exe -jar godzilla.jar
----------

# 也可以在文件夹下面调用子文件夹的exe文件
AntSword.bat
----------
cd /d %~dp0
start /b "AntSword" "AntSword-Loader/AntSword.exe"
----------
```

* [SecLists/](https://github.com/danielmiessler/SecLists)

```
# 字典文件，主要为其他工具提供字典，个人常用的字典主要是 https://github.com/danielmiessler/SecLists
```

* simple_tools/

```
# 这个是渗透小工具界面的目录，暂时还没开发，先留着。
```

* terminal_tools/

```
# 终端工具目录, 举几个栗子
- terminal_tools/dirsearch/
	- dirsearch.py
	- dirsearch.toml	*
	- *
最主要的就是这个dirsearch.toml文件，一定要和目录同名，因为程序是通过目录名索引的。
若目录名为: gobuster dir
则配置文件名: gobuster dir.toml
空格也要带上

文件内容就是给程序写一份文档:
name: 工具名称，直接显示在GUI界面标签上
pname: 运行工具需要的字符串
ppname: 运行工具所需要的环境，这里的环境不是本机的环境，是通过NNZ/res/env/env.toml文件获取到的对应环境路径。
参数分为三种must_args(必须参数)、nomust_noinput_args(可选选项参数)、nomust_input_args(可选输入参数)
[[must_args]]			# 必须参数
arg_name = "-u "		# 参数，注意-u后面加一个空格，用于拼接。这样设计的原因是有些参数没有空格比如: --exclude-size=2kb
arg_more = "添加目标url"		# 参数介绍，在GUI界面给人看的，随便写但是不要写太长了。
arg_text = "https://127.0.0.1"	# 参数默认值
arg_enable = true		# 默认是否启用
[[nomust_noinput_args]]		# 可选选项参数
arg_name = "-q "		# 参数，注意-q后面加一个空格
arg_more = "[必须开启]安静模式"	# 参数介绍，（一般要关闭滚动条，否则显示会很乱）
arg_enable = true		# 默认是否启用
[[nomust_input_args]]		# 可选输入参数
arg_name = "-x "		# 参数，注意-x后面加一个空格
arg_more = "过滤状态码"		# 参数介绍
arg_text = "404,502,301"	# 参数默认值
arg_enable = true		# 默认是否启用

以下为dirsearch.toml的配置文件，并没有写出所有功能，暂时只是记录了常用功能
---------------------
name = "dirsearch"
pname = "dirsearch.py"
ppname = "python3"		# 运行的时候通过env.toml文件获取环境路径python3 = "res/env/python3/python.exe"

[[must_args]]
arg_name = "-u "
arg_more = "添加目标url"
arg_text = "https://127.0.0.1"
arg_enable = true

[[nomust_noinput_args]]
arg_name = "-q "
arg_more = "[必须开启]安静模式"
arg_enable = true

[[nomust_noinput_args]]
arg_name = "-r "
arg_more = "递归扫描"
arg_enable = false

[[nomust_input_args]]
arg_name = "-x "
arg_more = "过滤状态码"
arg_text = "404,502,301"
arg_enable = true

[[nomust_input_args]]
arg_name = "--exclude-size="	# 参数加空格的罪魁祸首
arg_more = "过滤指定大小返回包"
arg_text = "2KB"
arg_enable = true

[[nomust_input_args]]
arg_name = "-w "
arg_more = "选择字典"
arg_text = "res/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt"	# 默认的字典位置，很方便的。
arg_enable = false
---------------------

# 对于gobuster这类工具，第一个参数是选择功能模块，那么将其各个功能分开单独创建文件夹
比如以下两个目录：
gobuster dir/
gobuster dns/
其中的exe文件命名可以不更改: gobuster.exe
在配置文件中将pname = "gobuster.exe"更改为：
pname = "gobuster.exe dir"、
pname = "gobuster.exe dns" 即可。
```

### 几份现有的配置文件，仅供参考

res/terminal_tools/dirsearch/dirsearch.toml

res/terminal_tools/fscan/fscan.toml

res/terminal_tools/ehole/ehole.toml	(该版本是Github上面拉下来最新代码自行构建的)

res/terminal_tools/gobuster dir/gobuster dir.toml

res/terminal_tools/gobuster dns/gobuster dns.toml
