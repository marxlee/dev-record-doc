# flume日志采集框架 1.7.0 and high版本
## Quick Start
安装简单容易配置, 只需要解压

```
cd /flume-1.7.0-bin/conf/
vi flume-env.sh

# 添加一行JAVA_HOME 目录, 即可
export JAVA_HOME=/opt/module/jdk1.8.0_191
```

## 编写conf
### 以我本身的项目为例
官方1.7文档: http://flume.apache.org/releases/content/1.7.0/FlumeUserGuide.html#taildir-source

#### 选择双层负载均衡策略
1. 第一层flume读取tomcat日志信息(日志信息info级别保存到固定的位置), 每台机器读取相应日志文件, flume负责分发到其他机器上, 方式 TAILDIR(1.7.0以上版本)
```
###TailDir###

a1.sources = r1
a1.channels = c1
a1.sinkgroups = g1
a1.sinks = k1 k2

a1.sources.r1.type = TAILDIR
a1.sources.r1.channels = c1
a1.sources.r1.positionFile = /opt/modules/flume/checkpoint/behavior/taildir_position.js
a1.sources.r1.filegroups = f1
a1.sources.r1.filegroups.f1 = /opt/collect_logs/log-collector-web/log-collector-web.log
a1.sources.r1.fileHeader = true

a1.channels.c1.type = file
a1.channels.c1.checkpointDir = /opt/space_flume/checkpoint/behavior/
a1.channels.c1.dataDirs = /opt/space_flume/data/behavior/
a1.channels.c1.maxFileSize = 104857600
a1.channels.c1.capacity = 90000000
a1.channels.c1.keep-alive = 60

a1.sinkgroups.g1.sinks = k1 k2
a1.sinkgroups.g1.processor.type = load_balance
a1.sinkgroups.g1.processor.backoff = true
a1.sinkgroups.g1.processor.selector = round_robin
a1.sinkgroups.g1.processor.selector.maxTimeOut=10000

a1.sinks.k1.type = avro
a1.sinks.k1.channel = c1
a1.sinks.k1.batchSize = 1
a1.sinks.k1.hostname = hadoop107
a1.sinks.k1.port = 1234

a1.sinks.k2.type = avro
a1.sinks.k2.channel = c1
a1.sinks.k2.batchSize = 1
a1.sinks.k2.hostname = hadoop108
a1.sinks.k2.port = 1234
```

2. 第二层接收第一层flume发来的数据 方式:avro, 注意配置项
官方1.7文档: http://flume.apache.org/releases/content/1.7.0/FlumeUserGuide.html#kafka-source
```
### avro ### 
a1.sources = r1
a1.channels = c1
a1.sinks = k1

a1.sources.r1.type = avro
a1.sources.r1.channels = c1
a1.sources.r1.bind = 0.0.0.0
a1.sources.r1.port = 1234

a1.channels.c1.type = file
a1.channels.c1.checkpointDir = /opt/space_flume/checkpoint/behavior_collect/
a1.channels.c1.dataDirs = /opt/space_flume/data/behavior_collect/
a1.channels.c1.maxFileSize = 104857600
a1.channels.c1.capacity = 90000000
a1.channels.c1.keep-alive = 60

# kafka consumer 需要注意的是, 1.7.0以上版本使用kafka配置信息是, 和1.6以下版本的是不一样的, 否则会无法启动消费kafka-topic
a1.sinks.k1.channel = c1
a1.sinks.k1.type = org.apache.flume.sink.kafka.KafkaSink
a1.sinks.k1.kafka.topic = collect-log-collector-web
a1.sinks.k1.kafka.bootstrap.servers = hadoop106:9092,hadoop107:9092,hadoop108:9092
a1.sinks.k1.kafka.flumeBatchSize = 1
a1.sinks.k1.kafka.producer.acks = 1

```



## 启动
```
# 1. 简单方式: 
bin/flume-ng agent --conf conf/ -f conf_example/example.conf -n a1 -Dflume.root.logger=INFO,console 
# 2. 官方文档: 
$ bin/flume-ng agent --conf conf --conf-file example.conf --name a1 -Dflume.root.logger=INFO,console
```

## 停止:
```
在/usr/lib/flume-ng中我没找到停止agent的命令。
官方解释为: 
1. kill <pid> 可以安全关闭, 而不是 kill -9 <pid>, 强制关闭可能导致数据丢失.
```

