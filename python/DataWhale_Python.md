# Python 
## Task1

### 1.环境搭建

1. anaconda环境配置
2. 解释器

使用 Pycharm 代替 Anaconda 环境

### 2.python初体验

1. print and input
```
print("hello world")
print(''hello python')

inputStr = input("请输入:")
```


### 3.python基础讲解

1. python 变量特性+命名规则
```
变量特征: 所有的变量都可以理解为内存中的一个对象的“引用”。类型是属于对象的，而不是变量。而对象有两种，
“可更改”与“不可更改”对象。在python中，strings，tuples和numbers是不可更改的对象，而list,dict,set等则属于可以修改的对象。
可变与不可变是有变


变量名命名:
1. 见名之意, 区分大小写, 使用小写, 单词与单词链接使用 "_"
2. 不能以"_" 以外的特殊字符开头
3. 不能以数字开头

例如: last_name = 号前后加一个空格

```

2. 注释方法
```
# 当行注释, linux系统相似, 使用一个 # 

"""
注释: 使用三对双引号, 中间括起来的部分,为注释部分
"""
```

3. python中“：”作用
```
def method () : 

if-else : 

for循环 : 

可以看出, ":" 后边是跟着函数体, 方法体结构

```
4. 学会使用dir()及和help()
```
"""
dir() 
函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；
带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。
如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
"""
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']

"""
help() 函数用于查看函数或模块用途的详细说明。
"""
>>> help()

Welcome to Python 3.7's help utility!

>>> dir
dir(...)
    dir([object]) -> list of strings

    If called without an argument, return the names in the current scope.
    Else, return an alphabetized list of names comprising (some of) the attributes
    of the given object, and of attributes reachable from it.
    If the object supplies a method named __dir__, it will be used; otherwise
    the default dir() logic is used and returns:
      for a module object: the module's attributes.
      for a class object:  its attributes, and recursively the attributes
        of its bases.
      for any other object: its attributes, its class's attributes, and
        recursively the attributes of its class's base classes.

```

import使用
```
"""
import 是外部py类的引用, 需要注意的是, 当引用外部依赖的会后, 需要弄清楚绝对路径, 否则pycharm会报红线错误, 虽然程序执行上没有问题
"""
```

pep8介绍
```
PEP8规范:
1. 每一级缩进使用4个空格。
2. 续行应该与其包裹元素对齐，要么使用圆括号、方括号和花括号内的隐式行连接来垂直对齐，要么使用挂行缩进对齐3。
   当使用挂行缩进时，应该考虑到第一行不应该有参数，以及使用缩进以区分自己是续行。
```

### 4.python数值基本知识

1. python中数值类型，int，float，bool，e记法等
```
str, int, bool, float, bool (True, False)
```

2. 算数运算符

| 符号|描述|实例|
|:--:|:---|:---|
|+	|加 - 两个对象相加|	a + b 输出结果 30|
|-	|减 - 得到负数或是一个数减去另一个数	|a - b 输出结果 -10|
|*	|乘 - 两个数相乘或是返回一个被重复若干次的字符串	|a * b 输出结果 200
|/	|除 - x除以y	|b / a 输出结果 2
|%	|取模 - 返回除法的余数	|b % a 输出结果 0
|**	|幂 - 返回x的y次幂	|a**b 为10的20次方， 输出结果 100000000000000000000
|//	|取整除 - 返回商的整数部分|（向下取整）|





3. 逻辑运算符

| 符号|描述|实例|
|:--:|:---|:---|
|and	|x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	|(a and b) 返回 20。|
|or	|x or y	布尔"或"	- 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。	|(a or b) 返回 10。|
|not	|not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	|not(a and b) 返回 False|


4. 成员运算符

| 符号|描述|实例|
|:--:|:---|:---|
|in	|如果在指定的序列中找到值返回 True，否则返回 False。	|x 在 y 序列中 , 如果 x 在 y 序列中返回 True。|
|not in	|如果在指定的序列中没有找到值返回 True，否则返回 False。	|x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。|



5. 身份运算符

| 符号|描述|实例|
|:--:|:---|:---|
|is	|is 是判断两个标识符是不是引用自一个对象|	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False|
|is not	|is not 是判断两个标识符是不是引用自不同对象|	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。|



6. 运算符优先级

| 符号|描述|
|:--:|:---|
|\*\*	                                        |指数 (最高优先级)|
|\~ \+ \-	                                    |按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)|
|\*  \/  \%  \/\/	                            |乘，除，取模和取整除|
|\+  \-	                                      |加法减法|
| >>  <<	                                    |右移，左移运算符|
|\&	                                          | 位  'AND'|
|\^  \|	                                      | 位运算符|
|\<= \< \> \>=	                              |比较运算符|
|\<\> \=\= \!\=	                              |等于运算符|
|\=  \%=  \/=  \/\/=  \-\=  \+\=  \*\=  \*\*=	|赋值运算符|
|is is not	                                  | 身份运算符|
|in not in	                                  | 成员运算符|
|not and or	                                  | 逻辑运算符|

问题: 暂时无问题

