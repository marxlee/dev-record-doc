
# HBase 学习笔记

## 一. 架构图
![架构](https://github.com/marxlee/Development-doc/blob/master/file/Hbase-架构1.jpg)

从图中可以看出Hbase是由Client、Zookeeper、Master、HRegionServer、HDFS等几个组件组成，下面来介绍一下几个组件的相关功能：
### 1）Client
Client包含了访问Hbase的接口，另外Client还维护了对应的cache来加速Hbase的访问，比如cache的.META.元数据的信息。

### 2）Zookeeper
HBase通过Zookeeper来做master的高可用、RegionServer的监控、元数据的入口以及集群配置的维护等工作。具体工作如下：
* 通过Zoopkeeper来保证集群中只有1个master在运行，如果master异常，会通过竞争机制产生新的master提供服务
* 通过Zoopkeeper来监控RegionServer的状态，当RegionSevrer有异常的时候，通过回调的形式通知Master RegionServer上下线的信息
* 通过Zoopkeeper存储元数据的统一入口地址

### 3）Hmaster
master节点的主要职责如下：
* 为RegionServer分配Region
* 维护整个集群的负载均衡
* 维护集群的元数据信息
* 发现失效的Region，并将失效的Region分配到正常的RegionServer上
* 当RegionSever失效的时候，协调对应Hlog的拆分

### 4）HregionServer
HregionServer直接对接用户的读写请求，是真正的“干活”的节点。  
它的功能概括如下：
* 管理master为其分配的Region
* 处理来自客户端的读写请求
* 负责和底层HDFS的交互，存储数据到HDFS
* 负责Region变大以后的拆分
* 负责Storefile的合并工作

### 5）HDFS
HDFS为Hbase提供最终的底层数据存储服务，同时为HBase提供高可用（Hlog存储在HDFS）的支持  
具体功能概括如下：
* 提供元数据和表数据的底层分布式存储服务
* 数据多副本，保证的高可靠和高可用性

## 二 HBase中的角色
### 1. HMaster
功能
* 1．监控RegionServer
* 2．处理RegionServer故障转移
* 3．处理元数据的变更
* 4．处理region的分配或转移
* 5．在空闲时间进行数据的负载均衡
* 6．通过Zookeeper发布自己的位置给客户端
### 2. RegionServer
功能
* 1．负责存储HBase的实际数据
* 2．处理分配给它的Region
* 3．刷新缓存到HDFS
* 4．维护Hlog
* 5．执行压缩
* 6．负责处理Region分片
### 3. 其他组件
* 1．Write-Ahead logs
HBase的修改记录，当对HBase读写数据的时候，数据不是直接写进磁盘，它会在内存中保留一段时间（时间以及数据量阈值可以设定）。但把数据保存在内存中可能有更高的概率引起数据丢失，为了解决这个问题，数据会先写在一个叫做Write-Ahead logfile的文件中，然后再写入内存中。所以在系统出现故障的时候，数据可以通过这个日志文件重建。
* 2．Region
Hbase表的分片，HBase表会根据RowKey值被切分成不同的region存储在RegionServer中，在一个RegionServer中可以有多个不同的region。
* 3．Store
HFile存储在Store中，一个Store对应HBase表中的一个列族。
* 4．MemStore
顾名思义，就是内存存储，位于内存中，用来保存当前的数据操作，所以当数据保存在WAL中之后，RegsionServer会在内存中存储键值对。
* 5．HFile
这是在磁盘上保存原始数据的实际的物理文件，是实际的存储文件。StoreFile是以Hfile的形式存储在HDFS的。





