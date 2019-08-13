# 单例

## 目标
1. 单例设计模式
2. \_\_new\_\_ 方法
3. Python 中的单例

## 01. 单例设计模式

设计模式:  
__设计模式__ 是 前人工作的总结和提炼，通常，被人们广泛流传的设计模式都是针对 __某一特定问题__ 的成熟的解决方案  
使用 __设计模式__ 是为了可重用代码、让代码更容易被他人理解、保证代码可靠性  

单例设计模式:  
目的 —— 让 __类__ 创建的对象，在系统中 __只有__ 唯一的一个实例  
每一次执行 __类名()__ 返回的对象，内存地址是相同的  
单例设计模式的应用场景  
__音乐播放__ 对象  
__回收站__ 对象  
__打印机__ 对象  
……


## 02. \_\_new\_\_ 方法
1. 使用 类名() 创建对象时，Python 的解释器 首先 会 调用 \_\_new\_\_ 方法为对象 分配空间
2. \_\_new\_\_ 是一个 由 object 基类提供的 内置的静态方法，主要作用有两个：
  1) 在内存中为对象 分配空间  
  2) 返回 对象的引用  
Python 的解释器获得对象的 __引用__ 后，将引用作为 __第一个参数__ ，传递给 \_\_init\_\_ 方法
重写 \_\_new\_\_ 方法 的代码非常固定 ！

重写 \_\_new\_\_ 方法 一定要 return super().\_\_new\_\_(cls)
否则 __Python__ 的解释器 __得不到__ 分配了空间的 __对象引用__ ，就不会调用对象的初始化方法
注意：\_\_new\_\_ 是一个静态方法，在调用时需要 主动传递 __cls__ 参数

![img](https://github.com/marxlee/Development-doc/blob/master/python/images/py_a6_1.png)

示例代码
```
class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        # 如果不返回任何结果，
        return super().__new__(cls)

    def __init__(self):
        print("初始化音乐播放对象")

player = MusicPlayer()

print(player)
```

## 03. Python 中的单例
单例 —— 让 __类__ 创建的对象，在系统中 __只有__ 唯一的一个实例
定义一个 __类属性__ ，初始值是 __None__，用于记录 __单例对象的引用__
重写 \_\_new\_\_ 方法
如果 __类属性__ __is None__ ，调用父类方法分配空间，并在类属性中记录结果
返回 __类属性__ 中记录的 __对象引用__

![img](https://github.com/marxlee/Development-doc/blob/master/python/images/py_a6_2.png)

```
class MusicPlayer(object):

    # 定义类属性记录单例对象引用
    instance = None

    def __new__(cls, *args, **kwargs):

        # 1. 判断类属性是否已经被赋值
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        # 2. 返回类属性的单例引用
        return cls.instance
```

__只执行一次初始化工作__ :  
在每次使用 __类名()__ 创建对象时，__Python__ 的解释器都会自动调用两个方法：  
\_\_new\_\_ 分配空间  
\_\_init\_\_ 对象初始化  
在上一小节对 \_\_new\_\_ 方法改造之后，每次都会得到 第一次被创建对象的引用  
但是：初始化方法还会被再次调用  

需求:  
让 初始化动作 只被 执行一次  

解决办法:  
定义一个类属性 __init\_flag__ 标记是否 __执行过初始化动作__ ，初始值为 __False__  
在 \_\_init\_\_ 方法中，判断 __init\_flag__ ，如果为 __False__ 就执行初始化动作  
然后将 __init\_flag__ 设置为 __True__  
这样，再次 __自动__ 调用 \_\_init\_\_ 方法时，__初始化动作就不会被再次执行__ 了  

```
class MusicPlayer(object):

    # 记录第一个被创建对象的引用
    instance = None
    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):

        # 1. 判断类属性是否是空对象
        if cls.instance is None:
            # 2. 调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3. 返回类属性保存的对象引用
        return cls.instance

    def __init__(self):

        if not MusicPlayer.init_flag:
            print("初始化音乐播放器")

            MusicPlayer.init_flag = True


# 创建多个对象
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)

```





