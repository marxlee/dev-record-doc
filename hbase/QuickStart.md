## Hbase Quick Start

### HBase的解压
#### 解压HBase到指定目录：
```
$ tar -zxvf hbase-1.3.1-bin.tar.gz -C /opt/module
```
### HBase的配置文件
#### 修改HBase对应的配置文件。目录: ~/hbase/conf/
```
1）hbase-env.sh修改内容：
export JAVA_HOME=/opt/module/jdk1.8.0_144
export HBASE_MANAGES_ZK=false       # 关闭hbase自带的zk管理器

2）hbase-site.xml修改内容：
<configuration>
	<property>     
		<name>hbase.rootdir</name>     
		<value>hdfs://hadoop102:9000/hbase</value>   
	</property>

	<property>   
		<name>hbase.cluster.distributed</name>
		<value>true</value>
	</property>

   <!-- 0.98后的新变动，之前版本没有.port,默认端口为60000 -->
	<property>
		<name>hbase.master.port</name>
		<value>16000</value>
	</property>

	<property>   
		<name>hbase.zookeeper.quorum</name>
	     <value>hadoop102:2181,hadoop103:2181,hadoop104:2181</value>
	</property>

	<property>   
		<name>hbase.zookeeper.property.dataDir</name>
	     <value>/opt/module/zookeeper-3.4.10/zkData</value>
	</property>
</configuration>

3）regionservers：
hadoop102
hadoop103
hadoop104

4) 软连接hadoop配置文件到hbase：
$ ln -s /opt/module/hadoop-2.7.2/etc/hadoop/core-site.xml /opt/module/hbase/conf/core-site.xml
$ ln -s /opt/module/hadoop-2.7.2/etc/hadoop/hdfs-site.xml /opt/module/hbase/conf/hdfs-site.xml

5) HBase远程发送到其他集群
$ scp -r hbase/ hadoop@hadoop103:$PWD
$ scp -r hbase/ hadoop@hadoop104:$PWD
```

### HBase服务的启动
```
1．启动方式1

$ bin/hbase-daemon.sh start master
$ bin/hbase-daemon.sh start regionserver

**** 提示：如果集群之间的节点时间不同步，会导致regionserver无法启动，抛出ClockOutOfSyncException异常。
修复提示：

a、同步时间服务
添加时间同步操作
b、属性：hbase.master.maxclockskew设置更大的值
<property>
        <name>hbase.master.maxclockskew</name>
        <value>180000</value>
        <description>Time difference of regionserver from master</description>
 </property>

2．启动方式2
$ bin/start-hbase.sh
对应的停止服务：
$ bin/stop-hbase.sh

```

### 查看HBase页面
启动成功后，可以通过“host:port”的方式来访问HBase管理页面，例如：part<16010>

http://hadoop102:16010 


