from distutils.core import setup

setup(name="hm_message",  # 包名
      version="1.0",  # 版本
      description="marx's 发送和接收消息模块",  # 描述信息
      long_description="完整的发送和接收消息模块",  # 完整描述信息
      author="itheima",  # 作者
      author_email="mailmarx@163.com",  # 作者邮箱
      url="https://github.com/marxlee",  # 主页
      py_modules=["hm_message.send_message",
                  "hm_message.receive_message"])
