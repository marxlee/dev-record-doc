### 1. 输入过程: input_str = input("please input: ")  
input 输入接受的数据都是 <class:str>  

### 2. 数据类型:  
  2.1 str, int, bool, float  
  bool (True, False)
  
### 3. 数据类型的计算:   
  3.1 str * str # 是不准许的  
  3.2 str * int  
  3.3 int * bool * float  # (bool 在进行计算的时候, 转换True:1/ false:0)  

### 4. 类型转换:  
  4.1 int(..)  
  4.2 float(..)  
```
print(bool("True")) # True  
print(bool("False"))  # True  
print(bool(0))  # False  
```     
     
### 5. 格式化输出: %  
  5.1 %d 十进制%06d表示6位整数  
  5.2 %f 浮点型%.04f表示小数点含有4位  
  5.3 %s 字符串  
  5.4 %% 输出  
  
```
name = "Marx"
age = 10
val = 20
price = 18.7364837
print("这个一个str类型 %s " % name)
print("这个一个int类型: %d, val %d" % (age, val))
print("这是一个float类型, 并保留四位: %.04f" % price)
```

### 6. 关键字:  
  import keyword  # 打印python关键字  
  print(keyword.kwlist)  
  'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',  
  'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from',  
  'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',  
  'raise', 'return', 'try', 'while', 'with', 'yield'  
     
变量名命名:   
  见名之意, 区分大小写, 使用小写, 单词与单词链接使用 "_"    
  
  例如: last_name = 号前后加一个空格  
    
### 7. if判断语句:  

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
  
  
### 8. 随机数
```
import random # 引用随机数工具包
# 获取随机数打印
rand_int = random.randint(12, 20) # 方法生成 [12, 20] 包含12, 20 的随机int数
print(rand_int)
rand_int = random.randint(20, 20) # 恒等 20
print(rand_int)
rand_int = random.randint(30, 20) # 报错, 下限需要小于上限
print(rand_int)

```

### 9. 执行三大件
1. 顺序执行, 程序自上而下顺序执行  
2. 分支执行, if-elif-else
3. 循环执行, while循环, 特定的代码重复执行

### 10. 循环执行
关键字: while, break, continue
```

"""
打印5次 hello python
"""
w_int = 1
while w_int <= 5:
    w_int += 1   # 累加条件一定要在continue之前
    print("hello python %d" % w_int)
    # 嵌套if判断: 
    if w_int == 3:
        w_int += 1 # 对累加器赋值
        print("在3的位置继续向下执行while循环")
        continue
    elif w_int == 4:
        print("在4的位置跳出while循环")
        break

print("Program is end")

# 运算符
"""
赋值运算符: 
= 赋值
+= 加等
-= 减等
*= 乘等
/= 除等
//+ 整除等
%= 取余等
**= 幂等
"""

# python中的计数原则: 从0开始, 非1开始

"""
计算0~100相加结果
累加器
"""
result = 0
i = 0
while i <= 100:
    result += i # 累加
    i += 1  # 计数器 +1
print("计算0~100相加结果: %d" % result)


# 循环嵌套合适
i = 0
while condition1:
    sample1
    ....
    while condition2:
      sample2

print("结束")

# 针对print换行操作, 在某种情况下, 可能不需要换行
print("不想换行", end="") # 在print()函数加入参数 end="" 即可
print("下一行")


"""
foreach循环方法
"""
nums = (1,2,3,4,5,8)
for i in nums:
    print(i)



"""
转义字符: 
\\  反斜杠
\'  '
\"  "
\t  tab
\n  换行
\r  回车
"""

```

### 11. 函数基础
函数调用: 

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


### 12. python中模块概念
1. 每一个py文件, 在项目中都是一个模块, 模块的命名(又称: 模块标识符), 和变量的命名规范是一样的  
2. 调取模块中的方法, 和参数, 首先需要import导入模块  
3. 在引用过程中(import), 会将引用的文件编译成pyc文件, 也就是编译二进制文件, 为了提高python程序中的运行速度, 使用的巧妙地方式  


### 13. 高级类型:(非数字类型) 可以当做一个容器
1. 字符串, 列表, 元祖, 字典  
2. 包含: 公共方法, 变量高级   
3. 都可以使用 for .. in .. : 遍历
4. index: 索引从 0 开始, 取值: list[index], 当超出index范围取值, Error: Index out of range  

### 14. 列表:List  

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

### 15. 元祖
1. 多个元素组成的序列  
2. 元祖不能修改  
3. 元祖用(.., .., .., ..)表示, 内部元素可以是不同类型  
4. 索引从 0 开始  

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
#### 元祖应用场景: 
* 作为函数的参数, 

* 格式字符串, 
```
# 用例: 
print("年龄: %d, 名字: %s " % (age, name)) # %后边的合一视为元祖
info_str = "年龄: %d, 名字: %s " % (age, name)
```
* 保护列表的数据安全, 将列表转换成元祖
```
list(元祖) # 列表转换成元祖
tuple(列表) # 元祖转行为列表
```

### 16. 字典(dictionary)
1. 无序的对象集合  
2. 列表是有序的对象集合  
3. 定义 {} 格式类似于 Json, 相较于其他的语言, 更像是映射   
4. 使用键值对存储数据 {key:value, key:value}   
5. 键是唯一的, 键可以是字符串, 也得以是其他数据类型   

```
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


#### 应用场景: 
1. 一般描述某些事物的详细信息   
2. 针对于字典中数据的操作, 需要注意的是, 如果字典中的字段不存在, 会Error异常, 下标越界, 依然会异常
3. 在开发中, 会把多个字典放在一个列表中 
```
# 将多个字典放在一个列表中
card_list = [
    {
      "name":"小明",
      "age":18
    },
    {
      "name":"小胡",
      "age":20
    }
]
# 打印字典列表
for i in card_list:
  print(i)

#   

```

### 17.字符串
1. 使用一串字符用一对\" 或者\' 表示一个字符串
2. 

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

### 18. 切片
1. 适用于字符串, 列表, 元祖  
2. 使用索引值限制范围, 范围不能超过索引值的范围, 从一个大的字符串, 列表, 元祖 "有序的" 集合中, 拆分出一个小的字符串  
3. 字典是无序的, 是使用键值对存储, 不适用

```
"""
字符串的切片
# 操作: 

正序和倒叙
正序: 索引值为整数, 起始索引 < 结束索引, 步长为"正"数
倒序: 索引值为负数, 起始索引的'绝对值' < 结束索引的'绝对值', 步长为"负"数

起始索引: 默认值:0
结束索引: 默认值:结尾
步长: 表示需要按照设定的数值, 跳跃截取字符串(默认为: 1)
字符串[ 起始索引: 结束索引: 步长 ] # 语法
"""
# 实例
str = "表示需要按照设定的数值, 跳跃截取字符串"
# 操作
str[:]
str[2:]
str[:6]
str[0:5]
str[::2]
str[-1::-1] # 倒叙
str[::-1] # 倒叙

```

### 19. 公共方法
#### 1. 内置函数
len(...)  # 统计长度  
del(...)  # 操作删除变量, 删除元素 两种方式: del 关键字  
max(...)  # 返回容器的最大值, (注意: 字典操作的时候, 比较的key)  
min(...)  # 返回容器的最小值, (注意: 字典操作的时候, 比较的key)  
cmp(item1, item2) # 比较两者 (python3.0 已经去掉) 使用比较运算符做同样的操作  

**比较运算符: 可以比较字符串, 元祖, 数值, 列表等数据类型的数据. (字典不能比较大小) **

#### 2. 运算符的高级用法: 
```
#1. +            # 拼接: 产生新的数据    
(1,2) + (3,4)   -> (1,2,3,4)    # (字符串, 列表, 元祖)

#2. *            # 重复: 产生新的数据    
(1,2) * 2       -> (1,2,1,2)    # (字符串, 列表, 元祖)  

#3. in           # 存在     
3 in (1,2,3)    -> True        # (字符串, 列表, 元祖, 字典(key))  

#4. not in       # 不存在   
4 not in (1,2,3) -> True      # (字符串, 列表, 元祖, 字典(key))  

#5. > >= =< < ==  # 比较运算   
(1,2,3) < (2,3,4)  -> True      # (字符串, 列表, 元祖)

#6. .extend(...)   # 拼接: 拼接到原来的数据
(1,2,3).extend((4,5)) -> (1,2,3,4,5)
# .append(obj)  # 拼接: 有所extend方法不同的是, append方法, 是将数据, 原有的样子保存到列表中
[1,2,3].append([4,5]) -> [1,2,3,[4,5]]


```


### 20. for循环完整
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
### 21. 执行py程序
增加: #! shebang操作
```
$ which python3
/local/bin/python3

python执行文件的路径 /local/bin/python3 添加到python_main.py文件模块的头部可执行shebang操作的符号后边, 如下
#! /local/bin/python3

# 为文件加入可执行权限
$ chmod +x python_main.py

# 执行linux文件操作, 即可运行程序
$ ./python_main.py

# 为了省略python3 执行命令前缀
```



### 22. 全局变量, 局部变量
#### 定义
1. 全局变量: 在函数体外定义的变量, 所有函数都可以使用  
2. 局部变量: 在函数体内定义的变量, 只有函数内部可以使用  

#### 生命周期
1. 局部变量: 调用方法调用时, 被创建, 函数执行结束完毕, 被回收  
2. 全局变量: 程序执行结束, 回收  

#### 命名
1. 局部变量: 不同函数局部变量可重名
2. 全局变量: 不同模块之间变量可重名 需要加上前缀 gl_ 或者 g_, 保证全局变量识别起来相对容易  



#### 注意使用:
1. 全局变量: 在函数中, 不准许对全局变量进行修改
2. 尽量少的使用全局变量, 引用过程中(import), 会将模块中的全局变量引用过来
3. 函数内部的变量名称于全局变量重名, 调用过程中, 优先调用函数内部局部变量, 而非全局变量,   
      也由此得出, 全局变量的值是不能被函数内部修改的, 这也是函数调用顺序的过程




```
"""
注释: 
public_arg = "全局变量"

def method():
    private_arg = "局部变量"
    执行代码
"""

"""
用例: 
1. 查看函数的变量执行关系
2. 全局变放在 **"执行函数"** 的上方, 保证下方的函数能够快速的访问变量

"""
num = 10  # 全局变量

# 没有修改全局变量
def demo1():
    num = 45
    print("局部变量定义: ",num)

# 调取全局变量
def demo2():
    print("全局变量: ", num)

# 使用global目标关键字定义在函数中使用全局变量
def demo3():
    global num  # 需要放在前边
    num = 99
    print("修改全局变量: ", num)
#    print(name)

demo1()
demo2()
demo3()



"""
# 如果有函数调用了这个变量, 程序会报错
Erro : 
  修改全局变量:  99
  demo3()
    File "/hello-python/com/python/unit1/unit2.py", line 17, in demo3
    print(name)
  NameError: name 'name' is not defined
"""
name = "10"

```

### 22. 代码结构

定义模块:  
   * shebang  
   * import 模块  
   * 全局变量  
   * 函数定义  
   * 执行代码  
   
   
### 23. 






