# 常见问题分析和解决

## 读取本地和hdfs文件
```
// 当集群模式配置到hadoop的hdfs上时, 需要读取本地文件, 可以使用file:///模式读取
sc.textFile("file:///Readme.txt")
// 默认情况是, 如果不加file:// 会默认读取 hadoop:9000/的目录下的文件
sc.textFile("/Readme.txt")

```

## Spark-streaming Checkpoint
### 1. 一个 Streaming Application 往往需要7*24不间断的跑，所以需要有抵御意外的能力（比如机器或者系统挂掉，JVM crash等）。  
为了让这成为可能，Spark Streaming需要 Checkpoint 足够多信息至一个具有容错设计的存储系统才能让Driver 从失败中恢复。
Spark Streaming 会 Checkpoint 两种类型的数据。
Metadata（元数据） Checkpointing - 保存定义了 Streaming 计算逻辑至类似 HDFS 的支持容错的存储系统。用来恢复 Driver，元数据包括：
 *	配置 —— 用于创建该 streaming application 的所有配置；
 *	DStream 操作 —— DStream 一系列的操作；
 *	未完成的 batches —— 那些提交了 job 但尚未执行或未完成的 batches。
 
### 2. Data（数据） Checkpointing - 保存已生成的RDD至可靠的存储。  
这在某些 stateful 转换中是需要的，
在这种转换中，生成 RDD 需要依赖前面的 batches，会导致依赖链随着时间而变长。为了避免这种没有尽头的变长，要定期将中间生成的 RDDs 保存到可靠存储来切断依赖链。
总之，Metadata Checkpointing 主要用来恢复 Driver； Data Checkpointing 对于stateful 转换操作是必要的。

### 3. 什么时候该启用 Checkpoint 呢？  
满足以下任一条件：
 *	使用了有状态的transformation操作——比如updateStateByKey（强制），或者reduceByKeyAndWindow操作（非强制），被使用了，那么Checkpoint目录要求是必须提供的，也就是必须开启Checkpoint机制，从而进行周期性的RDD Checkpoint；
 *	希望能从意外中恢复 Driver。
如果 streaming app 没有 stateful 操作，也允许 driver 挂掉后再次重启的进度丢失，就没有启用 Checkpoint的必要了。

### 4. Checkpoint间隔设置  
* Checkpoint的时间间隔设置方法如下：  
  dstream.checkpoint(checkpointInterval)  
* Checkpoint时间间隔设置原则：一般设置为batch时间间隔的5-10倍。  
* Checkpoint会增加存储开销、增加批次处理时间。当批次间隔较小（如1秒）时，checkpoint可能会减小operation吞吐量；
反之，checkpoint时间间隔较大会导致lineage和task数量增长。  


### 5. 优雅停止streaming
在相应的checkpoint目录创建一个空的文件夹, spark-streaming会检测到这个文件夹, 并执行相应停止操作. 保证程序在执行过程中, 关闭相应的进程, 释放rdd-storage 内存, 停止executer, driver.

