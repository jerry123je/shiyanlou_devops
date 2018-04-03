# Linux 简介与使用



## 1 实验介绍

### 1.1 实验内容

欢迎大家来到楼+ Linux 运维与 Devops 这个课程的知识海洋中。希望你能跟着楼楼的步伐一步一步的登上 Linux 运维这座高楼。本节实验主要为大家介绍了 Linux 操作系统的一些基础概念以及尽快的让大家能够融入到 Linux 运维的学习中去。 

> 为了保证可以在实验楼环境中完成本次实验，我们在实验基础上补充了一系列的实验指导，比如实验截图，代码注释，帮助您更好得实战。

> 如果您对于实验有疑惑或者建议可以随时在讨论区中提问，与同学们一起探讨。

### 1.2 实验知识点



+ Linux 的简介
+ Linux 的历史
+ Linux 的发行版
+ 终端和桌面环境
+ Linux 的一些简单命令操作
+ Linux 开源社区

## 2. Linux 的简介

Linux 是一套可以免费使用和自由传播的类 Unix 操作系统，并且是一个基于 `POSIX` 和 `UNIX` 的**多用户、多任务、支持多线程和多 CPU 的操作系统**。和我们熟悉的 Windows 操作系统（XP、7、8、10 等）以及 Mac OS 系统一样都是用于管理和控制计算机硬件和软件资源的计算机程序。不过，Linux 区别于其他操作系统的最突出的特点就是它是一款**完全免费且开放源代码(open source)的操作系统**。


Linux 作为一个操作系统主要包括内核和系统调用两个部分，介于 `硬件` 和 `应用程序` 之间，就像一座桥梁连通着底层硬件和用户之间的信息交流。

Lunix 能够运行主要的 UNIX 工具软件、应用程序和网络协议，同时也支持 `32` 位和 `64` 位硬件。（事实上严格来讲，Linux 这个单词只是表示 Linux 内核，不过实际生活中人们已经习惯将 Linux 来代表整个基于 Linux 内核，且使用 GNU 工程各种工具和数据库的操作系统。）

“Linux 之父” 的 `Linus Torvalds` 所开发的 Linux 可以在 `x86 架构` 下运行，同时可以被移植到其他主机上来运行。除此之外，Linux 还具有**完全免费、兼容 POSIX1.0 标准、多用户、多任务和支持多种平台**等优点。

## 3. Linux 的历史

在 Linux 之前，UNIX 经过长时间的发展已经是一个相当稳定且成熟的操作系统存在于世。

1977 年通过 `Bill Joy` 释出 BSD(Berkeley Software Distribution)，从而出现了 UNIX like 操作系统。

1984 年 `Andrew Tannenbaum` 开发出了 Minix 操作系统。

1984 年 `Richard Stall` 提倡自由软件，同时提出了 GUN 项目，规范出 GPL（General Public License） 模式。

在 1991 年`Torvalds`开发了 Linux 的内核，并且将其放在网络上供大家下载。

目前，Linux 的内核开发主要是两个版本，作为开发中版本的奇数版，如：`2.5.x`，主要用于测试和开发的环境；另一种是稳定版本的偶数版，如：`2.6.x`，主要适用于一般家庭或者企业环境中。

## 4. Linux 发行版本

Linux 操作系统从诞生、发展到现在已经推出了许多的版本，而每个版本都拥有相当一部分的用户。
下面列出的是当下比较常见的几款 Linux 发行版。

+ **Debian**

`Debian` 在运行起来极其稳定，这使得它非常适合用于服务器。Debian 平时维护三套正式的软件库和一套非免费软件库，它有 37500 多个软件包。Debian 使用 `apt` 或 `aptitude` 来安装和更新软件。
**Debian 操作系统比较适合系统管理员和高级用户。**

+ **Gentoo**

与 Debian 一样，`Gentoo` 操作系统也包含数量众多的软件包。Gentoo 并非以预编译的形式出现，而是每次需要针对每个系统进行编译。Gentoo  的安装和使用起来很困难；不过它也是最佳学习对象，可以进而了解 Linux 操作系统的内部运作原理。Gentoo 使用 `portage` 来安装和更新软件。
**Gentoo 操作系统适合对 Linux 已经完全驾轻就熟的用户。**


+ **Ubuntu**


`Ubuntu` 是 Debian 的一款衍生版，也是当今最受欢迎的免费操作系统。Ubuntu 侧重于市场的应用，在服务器、云计算和一些运行 Ubuntu Linux 的移动设备上。作为 Debian Gnu Linux 的一款衍生版，Ubuntu 的进程、外观和感觉大多数仍然与 Debian 一样。同样使用 `apt` 软件管理工具来安装和更新软件。
**Ubuntu 是新手用户最易上手的一款操作系统。**

+ **CentOS**


`CentOS` 是一款企业级 Linux 发行版，使用红帽企业级 Linux 中的免费源代码重新构建而成。这款重构版完全去掉了注册商标以及 Binary 程序包方面一个非常细微的变化。CentOS 的外观和行为似乎与母发行版红帽企业级 Linux 十分相似。 CentOS 使用 `YUM` 来管理软件包，是非常稳定的程序包。
**同样 CentOS 也是新手用户容易上手的一款操作系统。**

+ **Kali Linux**

`Kali Linux` 是 Debian 的一款衍生版。Kali 旨在用于渗透测试。Kali 的前身是 Backtrack。用于 Debian 的所有 Binary 软件包都可以安装到 Kali Linux 上。Kali 随带许多的渗透测试工具，无论是 Wifi、数据库还是其他任何工具，都设计成立马就可以使用。Kali 使用 `APT` 来管理软件包。
**Kali Linux 是一款渗透测试工具，或者可以说是文明黑客较为青睐的操作系统。**

## 5. 终端和桌面环境

### 5.1 终端

通常我们在使用 Linux 时，并不是直接与系统打交道，而是通过一个叫做 `Shell` 的中间程序来完成的。在图形界面下为了实现在一个窗口中完成用户输入和显示输出，Linux 系统还提供了一个叫做终端模拟器的程序（`Terminal`），下面是几个比较常见的终端模拟器：` gnome-terminal`，`Konsole`，`xterm`，`rxvt`，`kvt`，`nxterm` 和 `eterm` 。
目前我们的实验中的终端程序是 xfce 桌面环境自带的 `xfce-terminal` 。（不过要注意的是这里所说的终端（Terminal）和控制台（Console）是有区别的。）

### 5.2 实验楼桌面环境

如果你对当前实验桌面环境（xfce）的使用有任何困难，建议你先学习实验楼入门基础课程，对于其它桌面环境的使用，则不在本课程的范围之内，若有兴趣的用户可以在自己的计算机中安装完整的 Linux 发行版或其 Live CD 来进行体验。

[picture-1](https://dn-anything-about-doc.qbox.me/document-uid276733labid3904timestamp1509420016869.png/wm)

### 5.3 Xfce 终端

对于我们打开一个新的 `Xfce` 终端（双击桌面上的`Xfce` 终端打开），如下所示：

[picture-2](https://doc.shiyanlou.com/document-uid377240labid4104timestamp1512524218694.png/wm)

在界面中会出现一行 `shiyanlou:~/ $` 。下面简单介绍这一行内容的含义：

+ `shiyanlou`

    `shiyanlou` 代表的是当前用户的用户名，完整的格式应该为 `username@host` 。`username` 为用户名，`host` 为主机名，在线环境中使用的为 `Shell` 不会显示主机名。

+ `~/` 

    冒号后面的 `~/` 代表的是路径，会根据当前所处的文件路径变化，这里的 `~` 即波浪符号代表的是用户的家目录，对应于 `shiyanlou` 用户的家目录为 `/home/shiyanlou/`

+ `$`

    `$` 符号代表的是命令提示符，我们可以在命令提示符后面输入命令。命令提示符有两个，一个为 `$`，另一个为 `#` ，前者代表普通用户，后者代表 `root` 用户，即命令将使用超级管理员权限执行。

## 6 Linux 简单命令操作


**首先，我们双击需要打开桌面上的 `Xfce终端`，再学习下面的内容**

### 6.1 ls 命令



`ls` 命令主要用于显示文件的相关信息，默认情况下，`ls` 用来打印当前目录清单。同时，`ls` 命令还可以查看文件夹包含的文件以及查看目录、文件夹、文件权限等目录信息的内容。

如下图所示，**我们输入相应的命令后，敲回车键，执行命令**，会显示相应的结果：



[picture-3](https://dn-anything-about-doc.qbox.me/document-uid276733labid3904timestamp1509415092077.png/wm)

**语法**

```
ls [选项][参数]
```

选项说明

|选项|说明|
|-|-|
|`-a`|显示包含隐藏文件在内的所有文件|
|`-l`|以长格式显示目录下的内容列表。|
|`-d`|仅显示目录名，而不显示目录下的内容列表|
|`-r`|以文件反序排列并输出目录内容列表|
|`-k`|以 KB 为单位显示文件大小|
|……|……|



**举例**

eg 1：显示目录列表

```
$ ls 
```

eg 2：显示目录并列出隐藏文件



```
$ ls -a
```

eg 3：以长格式输出目录（显示文件和目录的详细信息）

```
$ ls -l
```

### 6.2 pwd 命令


`pwd` 命令主要用于显示当前用户的工作目录，可以得到用户目前所在的工作目录和绝对路径名称。

**语法**

```
pwd
```

**举例**

eg 1：显示当前工作目录

```
$ pwd
```

[picture-4](https://dn-anything-about-doc.qbox.me/document-uid276733labid3904timestamp1509415144281.png/wm)

### 6.3 cd 命令


用于在不同目录间切换，同时要确保有进入目的目录的权限。


eg 1：如下所示的使用绝对路径和相对路径进行切换目录。

```bash
# 切换到 /home 目录
shiyanlou:~/ $ cd /home
shiyanlou:/home/ $


# 查看 /home 目录下的文件和文件夹
shiyanlou:/home/ $ ls
shiyanlou

# 切换到 /home/shiyanlou  使用绝对路径
shiyanlou:/home/ $ cd /home/shiyanlou
shiyanlou:~/ $

# 再次切换到 /home 路径
shiyanlou:~/ $ cd /home
shiyanlou:/home/ $

# 使用相对路径切换到 /home/shiyanlou
shiyanlou:/home/ $ cd shiyanlou
shiyanlou:~/ $

# 最后还可以使用 ~ 符号切换到 shiyanlou 用户的家目录
shiyanlou:~/ $ cd /home
shiyanlou:/home/ $
shiyanlou:/home/ $ cd ~
shiyanlou:~/ $
```

### 6.4 wget 命令

用于从网络上下载文件或资源的命令，没有指定目录，下载资源将默认为当前目录。`wget` 支持 `HTTP`，`HTTPS` 和 `FTP` 协议，可以使用 `HTTP` 代理。

**语法**

```
wget[参数][下载网址]
```


**举例**

eg 1：使用 wget 从实验楼平台上下载单个文件。

```
$ wget http://labfile.oss.aliyuncs.com/courses/980/shiyanlou.txt
```

### 6.5 cp 命令

主要用于复制文件和目录，将一个或多个源文件复制到目标文件或目标目录，是 Linux 较常用的命令之一。

语法


```
cp[选项][源][目的目录]
```

选项说明

|选项|说明|
|-|-|
|`-a`|复制时保留源文档的所有属性，或者叫创建备份|
|`-r`|复制目录和目录里的所有项目|
|…|……|

**举例**

eg 1：复制 `/etc/hosts `文件到`/tmp/` 目录下。

```
$ cp /etc/hosts /tmp/
```

[picture-5](https://dn-anything-about-doc.qbox.me/document-uid276733labid3904timestamp1509415209196.png/wm)

eg 2：复制文件`/etc/hosts` 到 目录 `/tmp/` 下，并修改名称为`host`。

```
$ cp /etc/hosts /tmp/host
```

[picture-6](https://dn-anything-about-doc.qbox.me/document-uid276733labid3904timestamp1509415223629.png/wm)

### 6.6 rm 命令

主要用于删除一个目录中的一个或多个文件或目录，也可以将某个目录及其下的所有文件及子目录均删除。对于链接文件，只是删除了链接，原有文件均保持不变。（不过在使用的时候要特别小心这个命令）

**语法**

```
rm[选项][文件]
```

选项说明

|选项|说明|
|-|-|
|`-f`|忽略不存在的文件且不提示，强制删除|
|`-i`|删除前会有提示|
|`-r`|递归删除，将选项中列出的全部目录和子目录均递归地删除|
|……|……|

**举例**


eg 1：删除 `host` 文件，且逐一询问。

```
$ rm -i host
```


[picture-7](https://dn-anything-about-doc.qbox.me/document-uid276733labid3904timestamp1509415256985.png/wm)

### 6.7 mkdir 命令

用来创建指定的名称的目录，要求创建目录的用户在当前目录中具有写权限，并且指定的目录名不能是当前目录中已有的目录。

**语法**

```
mkdir[选项][目录]
```

选项说明

|选项|说明|
|-|-|
|`-p`|若路径中的某些目录尚不存在,加上此选项后,系统将自动建立好那些尚不存在的目录,即一次可以建立多个目录|
|……|……|

**举例**

eg 1：递归创建多个目录。

```
$ mkdir -p test1/test11
$ ll # 该命令用来列出文件下的所有文件信息。
$ cd test1
$ ll
```

[picture-8](https://dn-anything-about-doc.qbox.me/document-uid276733labid3904timestamp1509415283561.png/wm)

### 6.8 cat 命令

主要用于连接文件或标准输入并打印。常用来显示文件内容，或者将几个文件连接起来显示，或者从标准输入读取内容并显示，它常与重定向符号配合使用。


**语法**

```
cat[选项][文件]
```

选项说明

|选项|说明|
|-|-|
|`-A`|展示所有,等价于 -vET|
|`-b`|对非空输出行编号|
|`-n`|从 1 开始对输出的所有行数编号|
|……|……|

**举例**

eg 1：查看`/etc/passwd` 文件内容，并对文件进行非空行编号输出。

```
$ cat -b /etc/passwd
```

[picture-9](https://dn-anything-about-doc.qbox.me/document-uid276733labid3904timestamp1509415306416.png/wm)

## 7 Linux 开源社区


国外著名的 Linux 网站


+ [Linux Online](https://www.linux.org/)：最权威的 `Linux` 网站，有大量的文章、讨论，以及软件硬件等。
+ [Linux.com](https://www.linux.com/)：学习 Linux 的最好网站，也是 `Linux` 使用经验的汇聚地。
+ [Linuxforums](http://www.linuxforums.org/forum/)： 提供 `Linux` 的软件资源，`Linux` 论坛，`Linux` 服务器发行版的信息，LINUX 相关文章教程等信息的综合性网站。


国内专业的 Linux 网站（社区）

+ [Linux 公社](http://www.linuxidc.com/)：是专业的 Linux 系统门户网站，实时发布最新 Linux 资讯，包括 `Linux、Ubuntu、Fedora、RedHat、红旗 Linux、Linux 教程、Linux 认证、SUSE Linux、Android、Oracle、Hadoop` 等技术。
+ [LinuxCN](https://linux.cn/)：Linux 中国是专注于中文 Linux 技术、资讯的社区，在这里可以获得一手的 Linux 资讯和技术知识。
+ [ChinaUnix](http://www.chinaunix.net/)：是一个以讨论 `Linux/Unix` 类操作系统技术、软件开发技术、数据库技术和网络应用技术等为主的开源技术社区网站。 
+ [Linux 伊甸园论坛](http://www.linuxeden.com/)： 中文 `GNU/Linux` 开源社区，开源资讯门户网站，提供最新最快的 Linux 和开源资讯，24 小时滚动更新。

## 8 总结

本节主要是让大家初步认识**linux操作系统**，同时作为**楼 +** 的一个开始，希望大家能够有以下几点准备：


1.学习态度
+ `Linux ` 作为一门基础的入门课程，扎实的基础功是必不可少的。所以一定从**基础入手**，切勿好高骛远。
+ **多总结，多思考，多动手**。不管是哪一门学科语言，要想最终达到熟练掌握都是需要不断地努力去练习的。
+ 读书好问，一问不得，不妨再问。充分利用平台提供的**问答区**或者网络的力量，力求问题得到及时的解答。

2.学习路径

[picture-10](https://doc.shiyanlou.com/document-uid276733labid3904timestamp1512377297296.png/wm)