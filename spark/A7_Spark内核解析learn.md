# Spark 内核解析

## 运行模式解析
### standalone client



### standalone cluster

### yarn client

### yarn cluster

## 任务

### 任务调度
HDFS -> 多个Block块, block是hadoop-split结果, 一个spark-job运行是会分配多个stage, 一个stage会分配多个task, 一个task是一个partition的数据, 
一个partition则是一个split块数据, 在hdfs中, 一个split切片, 就是一个block块. 



