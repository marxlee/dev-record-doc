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


# Task2

## 1.列表
1. 标志
2. 基本操作(创建，append( )，pop( ) ,del( ), 拷贝）
3. 列表相关方法
```
"""
定义List:
使用[], 内部元素使用 "," 相隔  
"""
name_list = ["zhangshan", "lisi", "wangwu"] # 定义一个list
name_list[0]  # 取值使用下标

# 针对list操作的方法
name_list[1] = "修改内容" # 针对某一个位置上修改数据
name_list.append("new_name") # 末尾追加数据  
name_list.count("wangwu") # 元素出现的次数   
name_list.insert(1, "insert_name")  # 在 index = 1 的位置插入一条数据  
name_list.reverse()   # 反转列表
name_list.clear()     # 清理数据   
name_list.extend(["八戒","唐僧"]) # 追加一个列表的数据  
name_list.pop(index)     # 堆栈操作, pop 在列表尾部拿出一个元素, index参数可以不加参数, 会在末尾弹出一个元素
name_list.sort()    # 排序赋值给自己
name_list.copy()    # 赋值这个list列表
name_list.index("lisi") # 注意, 如果lisi不在列表中, 程序异常   
name_list.remove("wangwu")  # 删除  
len(name_list)  # 列表的长度
del name_list[1]  # 删除元素 使用关键字 del

for in 遍历
for i in name_list:
    print(i)

```

## 2.元组
1. 标志
2. 基本操作（创建及不可变性）
```
# 创建一个元祖
info_tuple = ("姓名", 10, 60.5)   
# 空元祖
nil_tuple = ()  
# 验证tuple
type(info_tuple) # <class:tuple>
# 取值, 不能超过元祖的下标值, 会出现下标越界 tulpe index out of range
info_tuple[0]
# 定义一个元素的元祖
single_tuple=(1,)
#取值
tuple(single_tuple)

# 元祖提供方法 
single_tuple.count(1)   # 统计
single_tuple.index(1)   # 下标值

# 循环遍历, 需求不高, 原因保存的数据类型不同, 想要对每个元素执行操作, 也是不方便的
for i in info_tuple:
    print(i, end="--")
# console:  姓名--10--60.5

```


## 3.string字符串
1. 定义及基本操作（+，*，读取方式）
2. 字符串相关方法

```
# 演示

# 双引号和单引号, 共同使用,只有当字符串里有\" 双引号的时候
str1 = '这是一个字符串: "abcd"' 
print(str1)

#取值
print(str1[1])

#遍历
for char in str1:
    print(char, end=":")
    
# 以下操作于列表中的操作基本一致
len(str1)
# index方法取下标, 如果这个字符串中没有, 报错error
str1.index("ab")
# 统计字符数量, 如果这个字符串没有, 返回值为0
str2.count("ab")

"""
提供了如下方法, 语法于其他语言基本一致, 类似java, 见名之意
str.capitalize(   str.format_map(   str.isnumeric(    str.maketrans(    str.split(
str.casefold(     str.index(        str.isprintable(  str.partition(    str.splitlines(
str.center(       str.isalnum(      str.isspace(      str.replace(      str.startswith(
str.count(        str.isalpha(      str.istitle(      str.rfind(        str.strip(
str.encode(       str.isascii(      str.isupper(      str.rindex(       str.swapcase(
str.endswith(     str.isdecimal(    str.join(         str.rjust(        str.title(
str.expandtabs(   str.isdigit(      str.ljust(        str.rpartition(   str.translate(
str.find(         str.isidentifier( str.lower(        str.rsplit(       str.upper(
str.format(       str.islower(      str.lstrip(       str.rstrip(       str.zfill(
"""
```



## 4.字符串格式化问题

```
"""
Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。

"""
print ("格式化: 字符串: %s 数字 %d " % ('小明', 10))

"""
%c	 格式化字符及其ASCII码
%s	 格式化字符串
%d	 格式化整数
%u	 格式化无符号整型
%o	 格式化无符号八进制数
%x	 格式化无符号十六进制数
%X	 格式化无符号十六进制数（大写）
%f	 格式化浮点数字，可指定小数点后的精度
%e	 用科学计数法格式化浮点数
%E	 作用同%e，用科学计数法格式化浮点数
%g	 %f和%e的简写
%G	 %f 和 %E 的简写
%p	 用十六进制数格式化变量的地址
"""
```

问题: 无

# Task3

## 1.dict字典

定义
创建
字典的方法
```
"""
无序的对象集合
列表是有序的对象集合
定义 {} 格式类似于 Json, 相较于其他的语言, 更像是映射
使用键值对存储数据 {key:value, key:value}
键是唯一的, 键可以是字符串, 也得以是其他数据类型
"""
# 字典中的数据, 是无序的状态
dic_person_xiaoming =  {"name":"小明",
                        "age":10,
                        "weight":60.2}

# 字典的长度
len(dic_person_xiaoming) 
# 所有的keys 的值
dic_person_xiaoming.keys()
# 所有的values 的值
dic_person_xiaoming.values()
# 获取的是所有的元祖
dic_person_xiaoming.items() 
# 取值(key: 不存在会报错)
dic_person_xiaoming["name"]


# 删除指定的内容(不存在会报错)
dic_person_xiaoming.pop("name")

# 修改值(如果key存在-update, 不存在-insert)
dic_person_xiaoming["name"] = "小明" 
# update 合并字典, 如果字典中含有原字典中的字段, 字段将"重新"赋值
dic_person_xiaoming.update({"gender":"1", "age":30})
# 当字段不存在, 新增字段, 如果字段存在, "不赋值"
dic_person_xiaoming.setdefault("weight",70)
```

## 2.集合

特性
创建
方法
```
"""
集合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
创建格式：
"""
parame = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# 或者
set(("hello"))

"""
add()	为集合添加元素
clear()	移除集合中的所有元素
copy()	拷贝一个集合
difference()	返回多个集合的差集
difference_update()	移除集合中的元素，该元素在指定的集合也存在。
discard()	删除集合中指定的元素
intersection()	返回集合的交集
intersection_update()	返回集合的交集。
isdisjoint()	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()	判断指定集合是否为该方法参数集合的子集。
issuperset()	判断该方法的参数集合是否为指定集合的子集
pop()	随机移除元素
remove()	移除指定元素
symmetric_difference()	返回两个集合中不重复的元素集合。
symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()	返回两个集合的并集
update()	给集合添加元素

"""


```

## 3.判断语句（要求掌握多条件判断）

```
"""
以下判断条件:
==
!=
<
>
<=
>=
"""

"""
1. 简单sample: 
if 判断条件:
    条件成立, 执行 (这行代码前有四个空格, tab和空格, 不要混用)
python if语句和其他语言不通, 其他语言可以添加 {} 表示当前判断语句需要执行代码块

输入预想判断的数据: 需要注意的是, 这里有个转换int(input("请输入年龄age : ")), 如果不转换的直接进行对比, 会报 TypeErro str() >= int()
if .. elif .. else .. if判断条件语句格式 
"""
age = int(input("请输入年龄age : ")) # 需要转换
if age >= 10:  # 判断年龄的if
    print("你的年龄超过10岁, %d" % age)
    print("相同缩进代码, 属于条件满足的代码块")
elif age < 5:  # else if 判断条件
    print("当前小于 5 %d" % age)
else:
    print("条件不成立")
 

"""
2. sample: 嵌套
逻辑运算符: 与and/ 或or/ 非not
拼接条件
if (condition1 and condition2) or (condition3 and condition4) or (condition5 and condition6):
    run result...

# 以下伪代码需要换行, 需要将所有的条件加入整体小括号, 按照严谨的缩进规则, 并且缩进"希望"的是和执行代码的缩进有所区别, 因此条件换行需要添加8个空格;
if ((condition1 and condition2) 
        or (condition3 and condition4) 
        or (condition5 and condition6)):  # 缩进更多 8个空格
    # 可以加个空行
    run result...
需要注意的是: not不是链接两个条件, 而是单独作为一个"非"条件处理
"""
num = int(input("输入数字: "))
if num != 3 and 2 < num < 12:
    print("数字(2, 12),并且不等于3, d=%d" % num)
elif 30 > num > 20 or num == 17:
    print("数字(20, 30),或者等于17, d=%d" % num)
elif not 40 < num < 50:
    print("数字不在(2,40)范围内, d=%d" % num)
else:
    print("判断条件不成立")

"""
字符串的判断: __eq__ 与 == 是用法相同的, 区别于其他语言, 以下代码我们复用以上的变量 num
嵌套使用if语句需要注意: 严格注意代码缩进(***), 保证程序的执行不会有问题
"""
holiday_name = "女人节"
if holiday_name.__eq__("圣诞"):
    print("圣诞简写")
    if num > 20
        print("num > 20")
elif holiday_name == "圣诞节":
    print("是圣诞节")
elif holiday_name.__contains__("女人"):
    print("包含\"女\"单词")

```

## 4.三目表达式
```
x=2
y=3
 
if x > y:
    print(x)
else:
    print(y)
 
 
res='aaaaa' if x > y else 'bbbbbbb'     #三元表达式
print(res)
```


## 5.循环语句

```
"""
循环体结构: 
for arg in list:
    循环体代码
else:
    循环结束后, 会执行的代码, 如果: "循环体中有 break, 在执行break后, 是不会执行else代码块的"
    
"""

"""
判断同学在不在字典中
"""
students = [
    {
    "name":"小妹"
    },
    {
    "name":"大妹"
    }
]
# 寻找同学
find_name = "小妹"
for str in students:
  # print(str)
  if find_name == str["name"]:  # 判断字典key -> value
      print("找到了同学: ", str)
      break # 如果循环跳出, 不执行else操作
else:
    print("没有找到同学哟~ %s " % find_name)

print("program end")

```


# Task 4
## 1.函数关键字
## 2.函数的定义
```
# 定义函数 def method ():
# 文件名称为: create_my_method.py 中定义函数 method_1
def method_1(arg1, arg2): # 定义函数名, 命名方式和变量命名一致
    需要运行的方法体(注意缩进)
    ......
    return ... # 最为返回值操作


# 引用过程
import com.python.unit1.un_create_def as my # 值得注意的是, 想要代码提示, 需要补全路径, 并且设置别名
# 调用类中的方法
result = my.method_1("1", "2") # 带有参数的方法, 可以添加强制字符串类型, result负责接收method_1函数的结果
```




## 3.函数参数与作用域
```
全局变量: 在函数体外定义的变量, 所有函数都可以使用
局部变量: 在函数体内定义的变量, 只有函数内部可以使用

生命周期
局部变量: 调用方法调用时, 被创建, 函数执行结束完毕, 被回收
全局变量: 程序执行结束, 回收

命名
局部变量: 不同函数局部变量可重名
全局变量: 不同模块之间变量可重名 需要加上前缀 gl_ 或者 g_, 保证全局变量识别起来相对容易

注意使用:
全局变量: 在函数中, 不准许对全局变量进行修改
尽量少的使用全局变量, 引用过程中(import), 会将模块中的全局变量引用过来
函数内部的变量名称于全局变量重名, 调用过程中, 优先调用函数内部局部变量, 而非全局变量,
也由此得出, 全局变量的值是不能被函数内部修改的, 这也是函数调用顺序的过程
```

## 4.函数返回值
```
使用return 返回函数体的数据
```

## 5.file

打开文件方式（读写两种方式）

文件对象的操作方法

学习对excel及csv文件进行操作


```
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
	
file.close()
关闭文件。关闭后文件不能再进行读写操作。
	
file.flush()
刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
	
file.fileno()
返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。
	
file.isatty()
如果文件连接到一个终端设备返回 True，否则返回 False。
	
file.next()
返回文件下一行。
	
file.read([size])
从文件读取指定的字节数，如果未给定或为负则读取所有。

	
file.readline([size])
读取整行，包括 "\n" 字符。

	
file.readlines([sizeint])
读取所有行并返回列表，若给定sizeint>0，则是设置一次读多少字节，这是为了减轻读取压力。

	
file.seek(offset[, whence])
设置文件当前位置

	
file.tell()
返回文件当前位置。

	
file.truncate([size])
截取文件，截取的字节通过size指定，默认为当前文件位置。

	
file.write(str)
将字符串写入文件，返回的是写入的字符长度。

	
file.writelines(sequence)
向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
```


## 6.os模块
```
1	
os.access(path, mode)
检验权限模式
2	
os.chdir(path)
改变当前工作目录
3	
os.chflags(path, flags)
设置路径的标记为数字标记。
4	
os.chmod(path, mode)
更改权限
5	
os.chown(path, uid, gid)
更改文件所有者
6	
os.chroot(path)
改变当前进程的根目录
7	
os.close(fd)
关闭文件描述符 fd
8	
os.closerange(fd_low, fd_high)
关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略
9	
os.dup(fd)
复制文件描述符 fd
10	
os.dup2(fd, fd2)
将一个文件描述符 fd 复制到另一个 fd2
11	
os.fchdir(fd)
通过文件描述符改变当前工作目录
12	
os.fchmod(fd, mode)
改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。
13	
os.fchown(fd, uid, gid)
修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。
14	
os.fdatasync(fd)
强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。
15	
os.fdopen(fd[, mode[, bufsize]])
通过文件描述符 fd 创建一个文件对象，并返回这个文件对象
16	
os.fpathconf(fd, name)
返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。
17	
os.fstat(fd)
返回文件描述符fd的状态，像stat()。
18	
os.fstatvfs(fd)
返回包含文件描述符fd的文件的文件系统的信息，Python 3.3 相等于 statvfs()。
19	
os.fsync(fd)
强制将文件描述符为fd的文件写入硬盘。
20	
os.ftruncate(fd, length)
裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。
21	
os.getcwd()
返回当前工作目录
22	
os.getcwdu()
返回一个当前工作目录的Unicode对象
23	
os.isatty(fd)
如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。
24	
os.lchflags(path, flags)
设置路径的标记为数字标记，类似 chflags()，但是没有软链接
25	
os.lchmod(path, mode)
修改连接文件权限
26	
os.lchown(path, uid, gid)
更改文件所有者，类似 chown，但是不追踪链接。
27	
os.link(src, dst)
创建硬链接，名为参数 dst，指向参数 src
28	
os.listdir(path)
返回path指定的文件夹包含的文件或文件夹的名字的列表。
29	
os.lseek(fd, pos, how)
设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始. 在unix，Windows中有效
30	
os.lstat(path)
像stat(),但是没有软链接
31	
os.major(device)
从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。
32	
os.makedev(major, minor)
以major和minor设备号组成一个原始设备号
33	
os.makedirs(path[, mode])
递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。
34	
os.minor(device)
从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。
35	
os.mkdir(path[, mode])
以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。
36	
os.mkfifo(path[, mode])
创建命名管道，mode 为数字，默认为 0666 (八进制)
37	
os.mknod(filename[, mode=0600, device])
创建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。

38	
os.open(file, flags[, mode])
打开一个文件，并且设置需要的打开选项，mode参数是可选的
39	
os.openpty()
打开一个新的伪终端对。返回 pty 和 tty的文件描述符。
40	
os.pathconf(path, name)
返回相关文件的系统配置信息。
41	
os.pipe()
创建一个管道. 返回一对文件描述符(r, w) 分别为读和写
42	
os.popen(command[, mode[, bufsize]])
从一个 command 打开一个管道
43	
os.read(fd, n)
从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。
44	
os.readlink(path)
返回软链接所指向的文件
45	
os.remove(path)
删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。

46	
os.removedirs(path)
递归删除目录。

47	
os.rename(src, dst)
重命名文件或目录，从 src 到 dst

48	
os.renames(old, new)
递归地对目录进行更名，也可以对文件进行更名。

49	
os.rmdir(path)
删除path指定的空目录，如果目录非空，则抛出一个OSError异常。

50	
os.stat(path)
获取path指定的路径的信息，功能等同于C API中的stat()系统调用。

51	
os.stat_float_times([newvalue])
决定stat_result是否以float对象显示时间戳

52	
os.statvfs(path)
获取指定路径的文件系统统计信息

53	
os.symlink(src, dst)
创建一个软链接

54	
os.tcgetpgrp(fd)
返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组

55	
os.tcsetpgrp(fd, pg)
设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。

56	
os.tempnam([dir[, prefix]])
Python3 中已删除。返回唯一的路径名用于创建临时文件。

57	
os.tmpfile()
Python3 中已删除。返回一个打开的模式为(w+b)的文件对象 .这文件对象没有文件夹入口，没有文件描述符，将会自动删除。

58	
os.tmpnam()
Python3 中已删除。为创建一个临时文件返回一个唯一的路径

59	
os.ttyname(fd)
返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。

60	
os.unlink(path)
删除文件路径

61	
os.utime(path, times)
返回指定的path文件的访问和修改的时间。
62	
os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
输出在文件夹中的文件名通过在树中游走，向上或者向下。

63	
os.write(fd, str)
写入字符串到文件描述符 fd中. 返回实际写入的字符串长度

64	
os.path 模块
获取文件的属性信息。
```

# Task 5
1.类和对象
```
 面向对象基本概念
我们之前学习的编程方式就是 面向过程 的
面相过程 和 面相对象，是两种不同的 编程方式
对比 面向过程 的特点，可以更好地了解什么是 面向对象
```

2.正则表达式
```
re.match函数
re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
re.match(pattern, string, flags=0)

```

3.re模块
```
正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。

Python 自1.5版本起增加了re 模块，它提供 Perl 风格的正则表达式模式。

re 模块使 Python 语言拥有全部的正则表达式功能。

compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。

re 模块也提供了与这些方法功能完全一致的函数，这些函数使用一个模式字符串做为它们的第一个参数。

本章节主要介绍 Python 中常用的正则表达式处理函数，如果你对正则表达式不了解，可以查看我们的 正则表达式 - 教程。
```


4.datetime模块学习
```
Python 程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能。

Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。

时间间隔是以秒为单位的浮点小数。

每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。

Python 的 time 模块下有很多函数可以转换常见日期格式。如函数time.time()用于获取当前时间戳, 如下实例:

#!/usr/bin/python3

import time;  # 引入time模块

ticks = time.time()
print ("当前时间戳为:", ticks)
以上实例输出结果：

当前时间戳为: 1459996086.7115328
```


5.http请求
```
1、发送请求

import requests #导入requests，然后就可以为所欲为了

#发送get请求

r0 = requests.get("http://yunweicai.com")

#发送post请求

r1 = requests.post("http://yunweicai.com",data={key:value})

#发送post请求，带json串

json_data = {"user":"yunweicai","op":"post"}

r11 = requesets.post("http://yunweicai.com",json=json_data)

#put、delete、head、optiions请求也很简单

r = requests.put('http://yunweicai.com/put', data = {'key':'value'})

r = requests.delete('http://yunweicai.com/delete')

r = requests.head('http://yunweicai.com/get')

r = requests.options('http://yunweicai.com/get')

2、URL参数

URL 的查询字符串(query string)传递某种数据。如果你是手工构建 URL，那么数据会以键/值对的形式置于 URL 中，跟在一个问号的后面。例如， yunweicai.com/get?key=val。

requests库操作就比较优雅了，requests 允许你使用 params 关键字参数，以一个字符串字典来提供这些参数。

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.get("http://yunweicai.com/get", params=payload)

通过打印输出该 URL，你能看到 URL 已被正确编码：

print(r.url)
```


# Task 6




