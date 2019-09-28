## Stanalone模式安装
```
1）上传并解压spark安装包
[hadoop@hadoop102 sorfware]$ tar -zxvf spark-2.1.1-bin-hadoop2.7.tgz -C /opt/module/
[hadoop@hadoop102 module]$ mv spark-2.1.1-bin-hadoop2.7 spark

2）进入spark安装目录下的conf文件夹
[hadoop@hadoop102 module]$ cd spark/conf/

3）修改配置文件名称
[hadoop@hadoop102 conf]$ mv slaves.template slaves
[hadoop@hadoop102 conf]$ mv spark-env.sh.template spark-env.sh

4）修改slave文件，添加work节点：
[hadoop@hadoop102 conf]$ vim slaves

hadoop102
hadoop103
hadoop104

5）修改spark-env.sh文件，添加如下配置： 46  47 行
[hadoop@hadoop102 conf]$ vim spark-env.sh
SPARK_MASTER_HOST=hadoop102
SPARK_MASTER_PORT=7077       服务端口

6）分发spark包
[hadoop@hadoop102 module]$ xsync spark/

7）启动
[hadoop@hadoop102 spark]$ sbin/start-all.sh
[hadoop@hadoop102 spark]$ util.sh 
================hadoop@hadoop102================
3330 Jps
3238 Worker
3163 Master
================hadoop@hadoop103================
2966 Jps
2908 Worker
================hadoop@hadoop104================
2978 Worker
3036 Jps
网页查看：hadoop102:8080
注意：如果遇到 “JAVA_HOME not set” 异常，可以在sbin目录下的spark-config.sh 文件中加入如下配置：
export JAVA_HOME=XXXX

8）提交任务&执行程序
[hadoop@hadoop102 spark]$ bin/spark-submit \       
--class org.apache.spark.examples.SparkPi \             主类
--master spark://hadoop102:7077 \                         master
--executor-memory 1G \										任务的资源
--total-executor-cores 2 \										
./examples/jars/spark-examples_2.11-2.1.1.jar \		jar包
100

##################################
./bin/spark-submit \
--class <main-class>
--master <master-url> \
--deploy-mode <deploy-mode> \
--conf <key>=<value> \
... # other options
<application-jar> \
[application-arguments]
参数说明：
--master spark://hadoop102:7077 指定Master的地址
--class: 你的应用的启动类 (如 org.apache.spark.examples.SparkPi)
--deploy-mode: 是否发布你的驱动到worker节点(cluster) 或者作为一个本地客户端 (client) (default: client)*
--conf: 任意的Spark配置属性， 格式key=value. 如果值包含空格，可以加引号“key=value” 
application-jar: 打包好的应用jar,包含依赖. 这个URL在集群中全局可见。 比如hdfs:// 共享存储系统， 如果是 file:// path， 那么所有的节点的path都包含同样的jar
application-arguments: 传给main()方法的参数
--executor-memory 1G 指定每个executor可用内存为1G
--total-executor-cores 2 指定每个executor使用的cup核数为2个

该算法是利用蒙特•卡罗算法求PI
```
![PI](https://github.com/marxlee/Development-doc/blob/master/spark/images/Spark-run-PI.jpg.jpg)

```

9）启动spark shell
/opt/module/spark/bin/spark-shell \
--master spark://hadoop102:7077 \
--executor-memory 1g \
--total-executor-cores 2

注意：如果启动spark shell时没有指定master地址，但是也可以正常启动spark shell和执行spark shell中的程序，其实是启动了spark的local模式，该模式仅在本机启动一个进程，没有与集群建立联系。
Spark Shell中已经默认将SparkContext类初始化为对象sc。用户代码如果需要用到，则直接应用sc即可      sparksession  是sparksql 
scala> sc.textFile("./word.txt")
.flatMap(_.split(" "))
.map((_,1))
.reduceByKey(_+_)
.collect

res0: Array[(String, Int)] = Array((hive,1), (atg,1), (spark,1), (hadoop,1), (hbase,1))

```

## Standalone HA配置

![HA](https://github.com/marxlee/Development-doc/blob/master/spark/images/Spark-ha%E9%83%A8%E7%BD%B2.jpg.jpg)
```
1）zookeeper正常安装并启动

2）修改spark-env.sh文件添加如下配置：
[hadoop@hadoop102 conf]$ vi spark-env.sh

注释掉如下内容：
#SPARK_MASTER_HOST=hadoop102
#SPARK_MASTER_PORT=7077
添加上如下内容：
export SPARK_DAEMON_JAVA_OPTS="
-Dspark.deploy.recoveryMode=ZOOKEEPER 
-Dspark.deploy.zookeeper.url=hadoop102,hadoop103,hadoop104 
-Dspark.deploy.zookeeper.dir=/spark"

3）分发配置文件
[hadoop@hadoop102 conf]$ xsync spark-env.sh

4）在hadoop102上启动全部节点
[hadoop@hadoop102 spark]$ sbin/start-all.sh

5）在hadoop103上单独启动master节点88
[hadoop@hadoop103 spark]$ sbin/start-master.sh

6）spark HA集群访问
/opt/module/spark/bin/spark-shell \
--master spark://hadoop102:7077,hadoop103:7077 \   单独指定102也能
--executor-memory 2g \
--total-executor-cores 2
```

## JobHistoryServer配置
```
1）修改spark-default.conf.template名称
[hadoop@hadoop102 conf]$ mv spark-defaults.conf.template spark-defaults.conf

2）修改spark-default.conf文件，开启Log：
[hadoop@hadoop102 conf]$ vi spark-defaults.conf
spark.eventLog.enabled           true
spark.eventLog.dir               hdfs://hadoop102:9000/directory  
注意：HDFS上的目录需要提前存在。

3）修改spark-env.sh文件，添加如下配置：
[hadoop@hadoop102 conf]$ vi spark-env.sh

export SPARK_HISTORY_OPTS="-Dspark.history.ui.port=4000 
-Dspark.history.retainedApplications=3 
-Dspark.history.fs.logDirectory=hdfs://hadoop102:9000/directory"
参数描述：
spark.eventLog.dir：Application在运行过程中所有的信息均记录在该属性指定的路径下； 
spark.history.ui.port=4000  调整WEBUI访问的端口号为4000
spark.history.fs.logDirectory=hdfs://hadoop102:9000/directory  配置了该属性后，在start-history-server.sh时就无需再显式的指定路径，Spark History Server页面只展示该指定路径下的信息
spark.history.retainedApplications=3   指定保存Application历史记录的个数，如果超过这个值，旧的应用程序信息将被删除，这个是内存中的应用数，而不是页面上显示的应用数。

4）分发配置文件
[hadoop@hadoop102 conf]$ xsync spark-defaults.conf
[hadoop@hadoop102 conf]$ xsync spark-env.sh

5）启动历史服务
[hadoop@hadoop102 spark]$ sbin/start-history-server.sh

6）再次执行任务长度。
[hadoop@hadoop102 spark]$ bin/spark-submit \
--class org.apache.spark.examples.SparkPi \
--master spark://hadoop102:7077 \
--executor-memory 1G \
--total-executor-cores 2 \
./examples/jars/spark-examples_2.11-2.1.1.jar \
100

7）查看历史服务
hadoop102:4000
```
![Run-job](https://github.com/marxlee/Development-doc/blob/master/spark/images/Spark-run-job.jpg.jpg)



## yarn集群的配置
```
1）修改hadoop配置文件yarn-site.xml,添加如下内容：

[hadoop@hadoop102 hadoop]$ vi yarn-site.xml
        <!--是否启动一个线程检查每个任务正使用的物理内存量，如果任务超出分配值，则直接将其杀掉，默认是true -->
        <property>
                <name>yarn.nodemanager.pmem-check-enabled</name>
                <value>false</value>
        </property>
        <!--是否启动一个线程检查每个任务正使用的虚拟内存量，如果任务超出分配值，则直接将其杀掉，默认是true -->
        <property>
                <name>yarn.nodemanager.vmem-check-enabled</name>
                <value>false</value>
        </property>
        
2）修改spark-env.sh，添加如下配置：
[hadoop@hadoop102 conf]$ vi spark-env.sh

YARN_CONF_DIR=/opt/module/hadoop-2.7.2/etc/hadoop  
HADOOP_CONF_DIR=/opt/module/hadoop-2.7.2/etc/hadoop 

3）分发配置文件
[hadoop@hadoop102 conf]$ xsync /opt/module/hadoop-2.7.2/etc/hadoop/yarn-site.xml
[hadoop@hadoop102 conf]$ xsync spark-env.sh

4）执行一个程序
[hadoop@hadoop102 spark]$ bin/spark-submit \
--class org.apache.spark.examples.SparkPi \
--master yarn \
--deploy-mode client \
./examples/jars/spark-examples_2.11-2.1.1.jar \
100
注意：在提交任务之前需启动HDFS以及YARN集群。

```

## 支持hive操作
1. 将hive配置文件: hive-site.xml -> ../../hive-1.2.2-bin/conf/hive-site.xml 使用软连接的形式加载到spark的conf目录中  
ln -s ../../hive-1.2.2-bin/conf/hive-site.xml


