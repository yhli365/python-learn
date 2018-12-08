# 零基础Python入门

零基础Python入门--课件代码下载.zip

## 开发环境
```
Anaconda https://www.anaconda.com/
PyCharm https://www.jetbrains.com/pycharm/

Anaconda3-5.3.0-Windows-x86_64.exe
pycharm-professional-2018.2.4.exe
```

## 课程大纲
```
零基础Python入门
-- 梁斌
第0课：课程介绍
第1课：程序设计基础
1.	计算机与程序设计
a.	计算机组成
b.	计算机工作过程
c.	程序执行过程
d.	程序编写步骤
2.	Python语言概述
a.	Python语言发展历史
b.	Python语言特点
c.	Python应用举例
3.	Python开发环境配置
a.	安装Anaconda
b.	集成开发环境—IDLE
c.	PyCharm配置及简单应用
d.	运行方式：交互式和文件式
第2课：案例1 -- 汇率兑换
1.	汇率兑换1.0
a.	缩进，注释
b.	变量与命名，关键字
c.	字符串，赋值
d.	Input()与print()
2.	汇率兑换2.0
a.	分支语句if else
3.	汇率兑换3.0
a.	循环语句while
4.	汇率兑换4.0
a.	函数的定义与调用
5.	汇率兑换5.0
a.	匿名函数lambda
第3课：案例2 -- 分形树的绘制
1.	五角星绘制
a.	turtle库
b.	复习循环操作
2.	重复不同大小的五角星绘制
a.	复习函数与循环
3.	重复不同大小的五角星绘制
a.	递归函数
4.	分形树的绘制
a.	递归函数的应用
第4课：案例3 -- 基础代谢率(BMR)计算
1.	BMR计算1.0
a.	数值类型及运算
2.	BMR计算2.0
a.	复习分支语句、循环语句及input()函数
3.	BMR计算3.0
a.	字符串操作
4.	BMR计算4.0
a.	异常处理
第5课：案例4 -- 52周存钱挑战
1.	52周存钱挑战1.0
a.	复习循环语句及字符串操作
2.	52周存钱挑战2.0
a.	列表的概念及操作
b.	运用math库进行计算
3.	52周存钱挑战3.0
a.	循环语句for
b.	range()函数 
4.	52周存钱挑战4.0
a.	函数的参数传递
b.	变量的作用范围
5.	52周存钱挑战5.0
a.	时间处理库datetime
第6课：案例5 -- 判断第几天
1.	判断第几天1.0
a.	组合数据类型：元组
2.	判断第几天2.0
a.	复习列表的使用
b.	理解列表和元组的区别
3.	判断第几天3.0
a.	组合数据类型：集合
b.	理解列表与集合的区别
4.	判断第几天4.0
a.	映射数据类型：字典
第7课：案例6 -- 判断密码强弱
1.	判断密码强弱1.0
a.	复习字符串与分支结构
2.	判断密码强弱2.0
a.	循环的跳出操作：break与continue
3.	判断密码强弱3.0
a.	文件操作：写操作
4.	判断密码强弱4.0
a.	文件操作：读操作
5.	判断密码强弱5.0
a.	面向过程编程vs面向对象编程
b.	Python类的定义与使用
6.	判断密码强弱6.0
a.	面向对象编程的特点：封装、继承、多态
第8课：案例7 -- 模拟掷骰子
1.	模拟掷骰子1.0
a.	random模块
2.	模拟掷骰子2.0
a.	zip()函数的使用
b.	复习字典的使用
3.	模拟掷骰子3.0
a.	Python绘图库matplotlib
b.	散点图的简单绘制
4.	模拟掷骰子4.0
a.	简单的数据分析
b.	matplotlib绘制直方图
5.	模拟掷骰子5.0
a.	科学计算库NumPy
b.	NumPy中的向量化操作
c.	使用NumPy进行简单的数据分析
第9课：案例8 -- 空气质量指数(AQI)计算及分析
1.	AQI计算1.0
a.	复习分支结构、函数及异常处理
2.	AQI计算2.0
a.	JSON文件格式及操作
3.	AQI计算3.0
a.	CSV文件格式及写操作
b.	理解JSON与CSV的关联及差别
4.	AQI计算4.0
a.	CSV文件的读操作
b.	os模块
5.	AQI计算5.0
a.	什么是网络爬虫
b.	request库
6.	AQI计算6.0
a.	beautifulsoup库
7.	AQI计算7.0
a.	巩固beautifulsoup库
8.	AQI计算8.0
a.	完整网络爬虫的编写与实现
9.	AQI计算9.0
a.	Pandas基础
b.	利用Pandas进行数据处理及分析
10.	AQI计算10.0
a.	数据清洗
b.	利用Pandas进行数据可视化
```


## Bugs
=============================

### ImportError: DLL load failed
```
>>>>>>>>>>lect08_v3.0.py
D:\yapp\python\Anaconda3\python.exe lect08/lect08_v3.0.py
Traceback (most recent call last):
  File "D:\yapp\python\Anaconda3\lib\site-packages\numpy\core\__init__.py", line 16, in <module>
    from . import multiarray
ImportError: DLL load failed: 找不到指定的模块。
<<<<<<<<<<
升级组件版本
1)Settings/Project Interpreter: Anaconda3/Python 3.7
numpy         1.15.1  --> 1.15.4
matplotlib    2.2.3   --> 3.0.2
```

### bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml
```
>>>>>>>>>>aqi_v6.0.py
请输入城市拼音：beijing
Traceback (most recent call last):
  File "Y:/gitcode/yhli365/python-learn/python3_course/lect09/aqi_v6.0.py", line 40, in <module>
    main()
  File "Y:/gitcode/yhli365/python-learn/python3_course/lect09/aqi_v6.0.py", line 35, in main
    city_aqi = get_city_aqi(city_pinyin)
  File "Y:/gitcode/yhli365/python-learn/python3_course/lect09/aqi_v6.0.py", line 17, in get_city_aqi
    soup = BeautifulSoup(r.text, 'lxml')
  File "D:\yapp\python\Anaconda3\lib\site-packages\bs4\__init__.py", line 198, in __init__
    % ",".join(features))
bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml. Do you need to install a parser library?
<<<<<<<<<<
网上好多说是新的库不支持，卸载新的换老的就可以了，我从4.1一直试到3.7.2都没用，后来仔细琢磨发现是新版本语法支持改变了 
解决方法：在报错代码中把函数参数中所有的"lxml"改成"html.parser"
例子：
bs = BeautifulSoup(r, 'lxml').find(
#改成 bs = BeautifulSoup(r, 'html.parser').find(
```
