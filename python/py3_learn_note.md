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

列表:List  

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



