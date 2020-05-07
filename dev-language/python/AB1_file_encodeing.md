# 文件编码
### 01. 文本文件的编码格式（科普）

文本文件存储的内容是基于 字符编码 的文件，常见的编码有 ASCII 编码，UNICODE 编码等  
Python 2.x 默认使用 ASCII 编码格式  
Python 3.x 默认使用 UTF-8 编码格式  

### 1.1 ASCII 编码和 UNICODE 编码
ASCII 编码  
计算机中只有 256 个 ASCII 字符  
一个 ASCII 在内存中占用 1 个字节 的空间  
8 个 0/1 的排列组合方式一共有 256 种，也就是 2 ** 8  
001_ASCII编码表1￼  
![img](./images/py_a9_3.png)

UTF-8 编码格式    
计算机中使用 1~6 个字节 来表示一个 UTF-8 字符，涵盖了 地球上几乎所有地区的文字  
大多数汉字会使用 3 个字节 表示  
UTF-8 是 UNICODE 编码的一种编码格式  

### 1.2 Ptyhon 2.x 中如何使用中文

1. Python 2.x 默认使用 ASCII 编码格式
2. Python 3.x 默认使用 UTF-8 编码格式

在 Python 2.x 文件的 第一行 增加以下代码，解释器会以 utf-8 编码来处理 python 文件   

```
# *-* coding:utf8 *-*
```
这方式是官方推荐使用的！  

也可以使用
```
# coding=utf8
```
unicode 字符串
在 Python 2.x 中，即使指定了文件使用 UTF-8 的编码格式，但是在遍历字符串时，仍然会 以字节为单位遍历 字符串  
要能够 正确的遍历字符串，在定义字符串时，需要 在字符串的引号前，增加一个小写字母 u，告诉解释器这是一个 unicode 字符串（使用 UTF-8 编码格式的字符串）  

```
# *-* coding:utf8 *-*

# 在字符串前，增加一个 `u` 表示这个字符串是一个 utf8 字符串
hello_str = u"你好世界"

print(hello_str)

for c in hello_str:
    print(c)
```

