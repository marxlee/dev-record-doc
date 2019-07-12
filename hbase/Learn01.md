
# HBase 学习笔记

## 一. 架构图
![Hbase架构](https://github.com/marxlee/Development-doc/blob/master/hbase/img/Hbase-架构1.jpg)

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


## HBase数据结构
### 1 RowKey
与nosql数据库们一样,RowKey是用来检索记录的主键。访问HBASE table中的行，只有三种方式：(20-100个字符)
* 1.通过单个RowKey访问
* 2.通过RowKey的range（正则）
* 3.全表扫描
RowKey行键 (RowKey)可以是任意字符串(最大长度是64KB，实际应用中长度一般为 10-100bytes)，在HBASE内部，RowKey保存为字节数组。存储时，数据按照RowKey的字典序(byte order)排序存储。设计RowKey时，要充分排序存储这个特性，将经常一起读取的行存储放到一起。(位置相关性)
### 2 Column Family
列族：HBASE表中的每个列，都归属于某个列族。列族是表的schema的一部 分(而列不是)，必须在使用表之前定义。列名都以列族作为前缀。例如 courses:history，courses:math都属于courses 这个列族。
### 3 Cell
由{rowkey, column Family:columu, version} 唯一确定的单元。cell中的数据是没有类型的，全部是字节码形式存贮。
关键字：无类型、字节码
### 4 Time Stamp
HBASE 中通过rowkey和columns确定的为一个存贮单元称为cell。
每个 cell都保存 着同一份数据的多个版本。版本通过时间戳来索引。
时间戳的类型是 64位整型。时间戳可以由HBASE(在数据写入时自动 )赋值，此时时间戳是精确到毫秒 的当前系统时间。
时间戳也可以由客户显式赋值。如果应用程序要避免数据版 本冲突，就必须自己生成具有唯一性的时间戳。
每个 cell中，不同版本的数据按照时间倒序排序，即最新的数据排在最前面。  
为了避免数据存在过多版本造成的的管理 (包括存贮和索引)负担，HBASE提供 了两种数据版本回收方式。
一是保存数据的最后n个版本，二是保存最近一段 时间内的版本（比如最近七天）。用户可以针对每个列族进行设置。  

### 5 命名空间
结构
![命名空间](https://github.com/marxlee/Development-doc/blob/master/hbase/img/Hbase命名空间.jpg)

*  Table：表，所有的表都是命名空间的成员，即表必属于某个命名空间，如果没有指定，则在default默认的命名空间中。
*  RegionServer group：一个命名空间包含了默认的RegionServer Group。
*  Permission：权限，命名空间能够让我们来定义访问控制列表ACL（Access Control List）。例如，创建表，读取表，删除，更新等等操作。
*  Quota：限额，可以强制一个命名空间可包含的region的数量。


## HBase原理
### 1. 读流程
![流程图](https://github.com/marxlee/Development-doc/blob/master/hbase/img/Hbase-读流程.jpg)

* 1. Client先访问zookeeper，从meta表读取region的位置，然后读取meta表中的数据。meta中又存储了用户表的region信息；
* 2. 根据namespace、表名和rowkey在meta表中找到对应的region信息；
* 3. 找到这个region对应的regionserver；
* 4. 查找对应的region；
* 5. 先从MemStore找数据，如果没有，再到BlockCache里面读；
* 6. BlockCache还没有，再到StoreFile上读(为了读取的效率)；
* 7. 如果是从StoreFile里面读取的数据，不是直接返回给客户端，而是先写入BlockCache，再返回给客户端。

### 2. 写流程
![流程图](https://github.com/marxlee/Development-doc/blob/master/hbase/img/Hbase-写流程.jpg)

* 1. Client向HregionServer发送写请求；
* 2. HregionServer将数据写到HLog（write ahead log）。为了数据的持久化和恢复；
* 3. HregionServer将数据写到内存（MemStore）；
* 4. 反馈Client写成功。

### 3 数据flush过程
* 1. 当MemStore数据达到阈值（默认是128M，老版本是64M），将数据刷到硬盘，将内存中的数据删除，同时删除HLog中的历史数据；
* 2. 并将数据存储到HDFS中；

### 4 数据合并过程
* 1. 当数据块达到4块，Hmaster将数据块加载到本地，进行合并；
* 2. 当合并的数据超过256M，进行拆分，将拆分后的Region分配给不同的HregionServer管理；
* 3. 当HregionServer宕机后，将HregionServer上的hlog拆分，然后分配给不同的HregionServer加载，修改.META.；
* 4. 注意：HLog会同步到HDFS。






