# 使用说明

## 0x0.前言

TOML格式的配置文件很简单，可以复制现有的模板修改。

包含各种工具的完全体过大，第三方应用的安全性也不能保障，因此Github上面就只能存放一下配置文件。

配置起来也很简单，宁配吗？

- 配: 请参考下方使用手册

- 不配：[百度网盘](https://pan.baidu.com)   (暂时还没有)

## 0x1.目录

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
  * runs/
    * BurpSuite/
      * BurpSuite.bat
      * BurpSuite.png
    * \*
  * **simple_tools/**
  * **terminal_tools/**
  * **crypto_tools/**
    * dirsearch/
      * dirsearch.py
      * dirsearch.toml
      * \*
    * gobuster dir/
      * gobuster.exe
      * gobuster dir.toml
  * SecLists/
  * images/

### 目录说明

#### NNZ/res/env/

> 用于存放运行环境以及运行环境的配置文件

```
python2
python3
jdk8
jdk11
env.toml
```

### NNZ/res/runs/

> 用户存放启动器相关文件。

```
BurpSuite/
    BurpSuite.jar
    BurpSuiteLoader.jar
    BurpSuite.bat
    BurpSuite.png
*
```

### NNZ/res/simple_tools

> 存放一些小工具的目录，开发中(有好的思路请猛地Call me)

```
1.生成随机身份信息
2.生成社工密码
3.生成反弹shell
4.生成一句话木马
5.生成一个八重神子
```

### NNZ/res/terminal_tools

> 存放终端工具的目录，通过创建进程调用，进程间通讯获取输出。

```
dirsearch/
    dirsearch.py
    dirsearch.toml
    *
```

### NNZ/res/crypto_tools

> 编码加密模块，这个计划得往后稍稍了。

### NNZ/res/wordlist/

> 专门存放字典的地方，算是集成一下，下面是几个推荐。

```
https://weakpass.com/
https://github.com/scipag/password-list/
https://github.com/danielmiessler/SecLists/
https://github.com/Legoclones/password-cracking
```

### NNZ/res/images/

> 图片文件夹，没啥好说的

## 0x2.配置文件

> 学了Rust才知道TOML配置文件，是真的简单。

### NNZ/res/env/env.toml

```Config.toml
# 用于记载便携式环境的位置,主要为terminal_tools提供索引, 终端工具中有一些时exe文件，所以加个None=''表示父进程为空。
# 此文件必须存在
java8 = "res/env/jdk8/bin/java.exe"
java11 = "res/env/jdk11/bin/java.exe"
python2 = "res/env/python2/python.exe"
python3 = "res/env/python3/python.exe"
None = ''
```

### NNZ/res/runs/
> 目录下方必须要有与目录**同名**的.bat、.png文件: 

- NNZ/res/runs/[name]/[name].bat
- NNZ/res/runs/[name]/[name].png

```
cd /d %~dp0     # 此命令的作用是切换到脚本所在目录
Start /B        # 此命令的作用是启用新进程运行命令，用法有三种

# 1.启动新进程，命名为[name]，运行程序为[name].exe，程序的参数跟在后面，需要全部添加双引号。
Start /B "[name]" "[name].exe" "arg1" "arg2"

# 2.省略自定义进程名，用exe的名称作为进程名(这个我不太确定)
Start /B "[name]" [name].exe arg1 arg2

# 3.无脑一句话. 但是对于名称中有空格的exe就不能这样写了。
Start /B [name].exe arg1 arg2

# #.对于java、python运行的程序或脚本，java.exe便是进程，[name].jar属于参数。
# #.另外建议使用javaw.exe，可以完整挂在后台运行。
Start /B ../../env/jdk8/bin/javaw.exe -jar test.jar # 这个进程的名称是javaw.exe
Start /B "test" "../../env/jdk8/bin/javaw.exe" "-jar" "test.jar"    # 这个进程的名称是test
```

添加启动器的方法很简单，下面举几个栗子

* BurpSuite/
    * BurpSuite.bat    *
    * BurpSuite.png    *
    * BurpSuite.jar
    * BurpSuiteLoader.jar
    * \*
```
BurpSuite.bat
-----------------------------------------------------------
cd /d %~dp0
start /B "BurpSuite" "javaw.exe" "-Xmx8G" "-Dfile.encoding=utf-8" "-noverify" "-javaagent:BurpSuiteLoader.jar" "-jar" "BurpSuite.jar" 
-----------------------------------------------------------
```
* Clash
    * Clash.bat
    * Clash.png
    * Clash for windows.exe
    * \*
```
Clash.bat
-----------------------------------------------------------
cd /d %~dp0
start /b "Clash" "Clash for Windows.exe"
-----------------------------------------------------------
```
* AntSword/
    * AntSword.bat
    * AntSword.png
    * AntSword-Loader
    * antSword-master
```
AntSword.bat
-----------------------------------------------------------
cd /d %~dp0
start /b "AntSword" "AntSword-Loader/AntSword.exe"
-----------------------------------------------------------
```

### NNZ/res/terminal_tools

> 目录下方必须要有与目录**同名**的.toml文件[name].toml

- NNZ/res/terminal_tools/[name]/[name].toml

配置模板
```toml
name = "dirsearch"          # 在界面中显示的名称
# 拼接的命令行参数为： "[ppname] [pname] [args]"
pname = "dirsearch.py"      # 
ppname = "python3"          # exe类的可以填"None"，这里是从env.toml中获取"python3"的路径

[[input_args]]              # 设置为必选参数，其实也可以没有
arg_name = "-u "            # 参数，记得带一个空格，原因等下会解释
arg_more = "添加目标url"     # 参数解释，显示在界面中，不要写的太长
arg_text = "https://127.0.0.1"  # 参数默认值
arg_enable = true

[[option_args]]             # 可选选项参数1
arg_name = "-q "            # 参数，带空格
arg_more = "[必须开启]安静模式" # 参数介绍
arg_enable = true           # 参数默认是否启用

[[option_args]]             # 可选输入参数
arg_name = "-w "            # 参数，带空格
arg_more = "选择字典"      # 参数介绍
arg_text = "res/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt"    # 参数默认值，相对nnz.exe的路径就可以，也可以用绝对路径。
arg_enable = true           # 参数默认是否开启

[[input_args]]              # 可选输入参数2
arg_name = "--timeout="     # 参数，不用带空格(前面的参数需要带空格是因为这个)
arg_more = "设置超时时间"    # 参数介绍
arg_text = "3"              # 参数默认值
arg_enable = false          # 参数默认是否开启
```
#### 小栗子

文件名可以用空格

* NNZ/res/terminal_tools/gobuster/ (目录可以有空格)  
    * gobuster.exe
    * gobuster.toml (要这样命名)

gobuster dir.toml
```toml
name = "gobuster"
pname = "gobuster.exe"
ppname = "None"

[[option_args]]
arg_name = "dns "
arg_more = "[1]子域名爆破"       # 多种模式，可以标记序号，区分各自参数
arg_enable = false

[[option_args]]
arg_name = "dir "
arg_more = "[2]目录爆破"
arg_enable = true

[[option_args]]
arg_name = "vhost "
arg_more = "[3]虚拟主机爆破"
arg_enable = false

[[option_args]]
arg_name = "fuzz "
arg_more = "[4]模糊测试"
arg_enable = false

[[option_args]]
arg_name = "-i "
arg_more = "[1]显示IP"
arg_enable = false

[[input_args]]
arg_name = "-d "
arg_more = "[1]指定域名"
arg_text = "baidu.com"
arg_enable = false

[[input_args]]
arg_name = "-r "
arg_more = "[1]指定dns服务器"
arg_text = "114.114.114.114"
arg_enable = false

[[input_args]]
arg_name = "-u "
arg_more = "[2]指定Url"
arg_text = "http://127.0.0.1"
arg_enable = true

[[option_args]]
arg_name = "-k "
arg_more = "[2]跳过tls验证"
arg_enable = true

[[option_args]]
arg_name = "-n "
arg_more = "[2]不显示状态码"
arg_enable = false

[[option_args]]
arg_name = "-v "
arg_more = "[2]详细输出"
arg_enable = true

[[option_args]]
arg_name = "-e "
arg_more = "[2]显示完整url"
arg_enable = true

[[input_args]]
arg_name = "-u "
arg_more = "[3]指定主机"
arg_text = "baidu.com"
arg_enable = false

[[input_args]]
arg_name = "-u "
arg_more = "[4]指定url"
arg_text = "http://127.0.0.1/tag.php?id=test"
arg_enable = false

[[input_args]]
arg_name = "-w "
arg_more = "选择字典"
arg_text = "res/wordlist/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt"
arg_enable = true

[[input_args]]
arg_name = "-t "
arg_more = "线程数量"
arg_text = "32"
arg_enable = false

[[input_args]]
arg_name = "--timeout "
arg_more = "超时时间"
arg_text = "1"
arg_enable = false

[[input_args]]
arg_name = "-o "
arg_more = "输出位置"
arg_text = ""
arg_enable = false

[[option_args]]
arg_name = "-z "
arg_more = "不显示进度"
arg_enable = true

[[option_args]]
arg_name = "--no-color "
arg_more = "去掉输出颜色"
arg_enable = true
```

### NNZ/res/simple_tools

> 暂无

### NNZ/res/crypto_tools

> 暂无