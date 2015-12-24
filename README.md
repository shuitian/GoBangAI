 # GoBangAI
### 项目源码文件夹介绍
- src
	- python代码
- docs
	- 文档
- setup.py
	- 安装代码
- setup.bat
	- windows下实际安装文件

### 项目中间文件以及可执行程序介绍
- build
	- 中间文件夹
- dist
	- 可执行程序

## 五子棋AI需求分析说明书
版本 **1.0**
### 概述
本说明书适用于指导软件开发者开发五子棋AI项目。项目地址为[GoBangAI](https://github.com/shuitian/GoBangAI)
#### 角色定义
- 棋局
- 玩家
	- **玩家是由AI控制**
	- **玩家是由人控制**

#### 环境
- window环境
- python2.7
- [pygame 1.91](http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi)

### 功能性需求
#### 棋局模块
- 开始一盘游戏
	- 初始化游戏
		- 人可以在初始化时选择先手或者后守
		- 不选择系统将随机先手后手
		- AI对AI将随机先手后手
		- 棋盘大小可以随机或者固定或者由玩家决定，由设计说明书给出
	- 记录玩家信息，游戏数据
		- AI对AI
		- 人对AI
		- 先手是哪方
		- 棋盘大小
- 结束一盘游戏
	- 记录游戏数据
		- 哪方胜利
		- 在哪一回合胜利
		- 游戏耗时
	- 显示游戏信息
		- 类似XXX win的信息
- 显示统计信息
	- 玩家胜率
		- 先手胜率
		- 后手胜率

#### 玩家模块
- 落子
	- 选择棋盘上没有子的一个点，落子
- 认输
	- AI不会认输
	- 玩家可以在自己回合认输
	- 认输意味着**游戏结束**

#### 五子棋AI模块
- 根据当前棋局选择一个点来落子

### 非功能性需求
- 打开软件到界面出现的时间不能超过0.5秒
- AI的响应速度不能超过0.5秒
- 每次落子需要提示声音
- 棋局需要标示棋盘上上次落子的具体位置
- 游戏的声音可以调节


## 五子棋AI设计说明书
###数据表设计
该项目中，数据表是为了存储游戏概要信息而设计的，而不是存储游戏过程中的落子信息。项目使用sqlite作为数据库，**表中所有字段都是以字符串形式存储**。

####游戏表game
- id
	- 主键
	- 棋局id，唯一，在开局的时候随机生成或者累加
- startTime
	- 游戏开始时间
- endTime
	- 游戏结束时间
- firstHandName
	- 先手姓名
- secondHandName
	- 后手姓名
- winner
	- 胜利者的姓名
- round
	- 游戏在第几回合胜利
	- 两方都下一子为一回合
- width
	- 棋盘宽度
- heigth
	- 棋盘高度

####玩家表player
- name
	- 主键
	- 每个玩家拥有一个唯一的姓名
	- AI的姓名随机或者从名字表中选取
- ai
	- 该玩家是不是由ai控制
	- `True`
	- `False`

