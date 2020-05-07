## Apache项目, 分布式消息应用, 具有很高的扩展性, 高的吞吐量, 大数据中扮演着很重要的角色
下载地址:
http://kafka.apache.org/downloads

版本号: 
kafka_2.11-0.11.0.2

解压和修改配置文件
解压到当前目录下: 
```
$ tar -zxvf kafka_2.11-0.11.0.2.tgz -C ./
```

进入到config目录下: 
```
$ vi server.properties
```
```
#打开注释, 表示, topic可以删除

delete.topic.enable=true

# zookeeper地址:多个是用 "," 隔开

zookeeper.connect=hadoop106:2181,hadoop107:2181,hadoop108:2181

#设置位置标识(这里我配置的是我机器的ip号)

broker.id=106

#设置log生成地址(绝对路径)

log.dirs=/opt/module/kafka_2.11-0.11.0.2/kafkaLogs

退出vi
```

在kafka目录下穿件一个文件夹存放log日志
```
$ mkdir kafkaLogs
```


scp 分发到其他机器上, 注意: broker.id的其他机器上需要修改, 集群中必须唯一.

启动:(分别在集群机器上后台启动)
```
$ bin/kafka-server-start.sh config/server.properties 1>dev/null 2>&1  已过期

$ bin/kafka-server-start.sh -daemon config/server.properties
```
停止: (分别在集群的其他机器上停止)
```
$ bin/kafka-server-stop.sh 
```
演示功能: (这里使用机器号hadoop106做演示, 当然集群下使用其他的机器一样的效果)  
一. 创建topic
```
$ bin/kafka-topics.sh --zookeeper hadoop106:2181 --create --replication-factor 3 --partitions 3 --topic topic_name

1.replication-factor : 副本数量

2.partitions : 分区数量

3.topic : 定义topic名称
```
二. 查看topic列表
```
$ bin/kafka-topics.sh --zookeeper hadoop106 --list
```
三. 删除topic
```
$ bin/kafka-topics.sh --zookeeper hadoop106 --delete --topic topic_name
```
四. 生产者producer (注意: 端口号9092是producer端口号)
```
$ bin/kafka-console-producer.sh --broker-list hadoop106:9092 --topic topic_name
```
五. 消费者consumer(把所有的消息打印到控制台上)
```
$ bin/kafka-console-consumer.sh --zookeeper hadoop106:2181 --from-beginning --topic topic_name
```
六.查看topic详细信息
```
$ bin/kafka-topics.sh --zookeeper hadoop106:2181 --describe --topic topic_name
```


