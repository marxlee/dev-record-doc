# 多态

## 目标
多态
面向对象三大特性

## 封装 根据 职责 将 属性 和 方法 封装 到一个抽象的 类 中
定义类的准则
继承 实现代码的重用，相同的代码不需要重复的编写
设计类的技巧
子类针对自己特有的需求，编写特定的代码
多态 不同的 子类对象 调用相同的 父类方法，产生不同的执行结果

## 多态 可以 增加代码的灵活度
以 继承 和 重写父类方法 为前提  
是调用方法的技巧，不会影响到类的内部设计  
016_多态示意图￼
![img](https://github.com/marxlee/Development-doc/blob/master/python/images/py_a4_1.png)

## 多态案例演练
需求
在 Dog 类中封装方法 __game__  
普通狗只是简单的玩耍    
定义  __XiaoTianDog__ 继承自  __Dog__  ，并且重写 __game__ 方法  
哮天犬需要在天上玩耍  
定义 Person 类，并且封装一个 __和狗玩__ 的方法  
在方法内部，直接让 狗对象 调用 __game__ 方法  

016_多态￼  
![img](https://github.com/marxlee/Development-doc/blob/master/python/images/py_a4_2.png)

案例小结:  

Person 类中只需要让 __狗对象__ 调用 __game__ 方法，而不关心具体是 __什么狗__  
game 方法是在 __Dog__ 父类中定义的  
在程序执行时，传入不同的 __狗对象__ 实参，就会产生不同的执行效果  
多态 更容易编写出出通用的代码，做出通用的编程，以适应需求的不断变化！  

```
class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍..." % self.name)


class XiaoTianDog(Dog):

    def game(self):
        print("%s 飞到天上去玩耍..." % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):

        print("%s 和 %s 快乐的玩耍..." % (self.name, dog.name))

        # 让狗玩耍
        dog.game()


# 1. 创建一个狗对象
# wangcai = Dog("旺财")
wangcai = XiaoTianDog("飞天旺财")

# 2. 创建一个小明对象
xiaoming = Person("小明")

# 3. 让小明调用和狗玩的方法
xiaoming.game_with_dog(wangcai)
        
```        


