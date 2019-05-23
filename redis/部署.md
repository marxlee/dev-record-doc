
#编译:
安装顺利的情况下
```
tar -zxvf redis-3.0.7 -C ./


cd redis-3.0.7

make && make install

```

编译报错的情况下需要清除错误文件

```
make
# 报错 原因含有残留文件
make distclean

```

Redis Test 可以不用执行



#启动: 

编译结束后, 将原有的redis.conf复制一份 redis.conf.bk

```
#启动redis
$ src/redis-server ./redis.conf
# 访问客户端
$ src/redis-cli -h hadoop106 
# 查看进程
$ ps -ef|grep redis
# 关闭redis
$ src/redis-cli -h hadoop106 -p 6379 shutdown
```



