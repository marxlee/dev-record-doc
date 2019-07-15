# Hbase-Java api

## 1. pom.xml 依赖: 
```
        <dependency>
            <groupId>org.apache.hbase</groupId>
            <artifactId>hbase-server</artifactId>
            <version>1.3.1</version>
        </dependency>

        <dependency>
            <groupId>org.apache.hbase</groupId>
            <artifactId>hbase-client</artifactId>
            <version>1.3.1</version>
        </dependency>

```
## 2. 相关操作api
### 1. 创建连接

```
    // 连接操作
    private static Connection connection = null;
    private static Admin admin = null;

    // 抽取出来, 建立连接
    static {
        Configuration conf = HBaseConfiguration.create();
        conf.set(HConstants.ZOOKEEPER_QUORUM,"hadoop106:2181,hadoop107:2181,hadoop108:2181");
        try {
            connection = ConnectionFactory.createConnection(conf);

            admin = connection.getAdmin();

        } catch (IOException e) {
            e.printStackTrace();
        }

    }
    
    // 关闭连接操作
    public static void close(Connection connection, Admin admin){
        if(connection != null){
            try {
                connection.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        if(admin != null){
            try {
                admin.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

```

### 2. 创建表

```
    // 检测表是否存在
    public boolean tableExists(String tableName){
        boolean b = true;
        try {
            b = admin.tableExists(TableName.valueOf(tableName));
        } catch (IOException e) {
            e.printStackTrace();
        }
        // 一个业务的结束, 在判断这个链接结束
        // hbase: client.RpcRetryingCaller: Call exception, tries=10, retries=35, started=38241 ms ago, cancelled=false, msg=org.apache.hadoop.hbase.DoNotRetryIOException: Connection was closed while trying to get master
        close(connection, admin);
        return b;
    }
    
    
     /**
     * 创建表
     * @param tableName
     * @param columnFamilys
     * @return
     * @throws IOException
     */
    public boolean createTable (String tableName, List<String> columnFamilys) {
        // 检测表存在
        boolean b = this.tableExists(tableName);
        if(b){
            System.out.println("表"+tableName+"已存在");
            return false;
        }

        // 创建表方法
        HTableDescriptor hTableDescriptor = new HTableDescriptor(TableName.valueOf(tableName));
        for (String cf: columnFamilys) {
            HColumnDescriptor hColumnDescriptor = new HColumnDescriptor(cf);
            hColumnDescriptor.setVersions(1, 3);
            hTableDescriptor.addFamily(hColumnDescriptor);
        }
        try {
            admin.createTable(hTableDescriptor);
        } catch (IOException e) {
            e.printStackTrace();
        }
        // hbase: client.RpcRetryingCaller: Call exception, tries=10, retries=35, started=38241 ms ago, cancelled=false, msg=org.apache.hadoop.hbase.DoNotRetryIOException: Connection was closed while trying to get master
        // close(connection, admin);
        

        return true;
    }

```
### 3. 删除表
```

     public void dropTable(String tableName){
        try {
            if(!this.tableExists(tableName)){
                System.out.println("表不存在");
                return;
            }
            // 将表不可用操作, 首先disable表, 是当前表不可用
            admin.disableTable(TableName.valueOf(tableName));
            // 再删除, 演示不涉及到"其他"命名空间 namespace, 所以直接删除表操作
            admin.deleteTable(TableName.valueOf(tableName));
        } catch (IOException e) {
            e.printStackTrace();
        }
     }

```

### 4. 插入数据

```
    /**
     * 添加一条数据
     * @param tableName
     * @param rowkey
     * @param cf
     * @param cn
     * @param val
     */
    public void put(String tableName, String rowkey, String cf, String cn, String val){
        // 检测表的存在, 列祖不存在的情况下, 会抛出异常        
        try {
            Table table = connection.getTable(TableName.valueOf(tableName));
            Put put = new Put(Bytes.toBytes(rowkey));
            put.addColumn(Bytes.toBytes(cf), Bytes.toBytes(cn), Bytes.toBytes(val));
            List<Put> puts = new ArrayList<>();
            puts.add(put);
            // table.put(put);  // 单条插询
            table.put(puts);
            table.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }  
    
```

### 5. 插询一条rowKey数据
```
/**
     * 获取一条数据
     * @param tableName
     * @param rowKey
     */
    public void get(String tableName, String rowKey){
        try {
            Table table = connection.getTable(TableName.valueOf(tableName));
            Get get = new Get(Bytes.toBytes(rowKey));
//            get.addColumn("");
//            get.addFamily("");
            Result result = table.get(get);
            Cell[] cells = result.rawCells();
            for (Cell cell: cells) {
                System.out.println(Bytes.toString(CellUtil.cloneRow(cell)) + ", " + Bytes.toString(CellUtil.cloneFamily(cell)) + ", "
                        + Bytes.toString(CellUtil.cloneQualifier(cell)) + ", " + Bytes.toString(CellUtil.cloneValue(cell))
                );
            }
            table.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
```
### 6. 列祖的数据
```
    /**
     * 扫描表 
     * @param tableName
     */
    public void scanner(String tableName){
        try {
            Table table = connection.getTable(TableName.valueOf(tableName));
            Scan scan = new Scan();
            ResultScanner scanner = table.getScanner(scan);
            for (Result result: scanner) {
                Cell[] cells = result.rawCells();
                for (Cell cell: cells) {
                    System.out.println(Bytes.toString(CellUtil.cloneRow(cell)) + ", " + Bytes.toString(CellUtil.cloneFamily(cell)) + ", "
                            + Bytes.toString(CellUtil.cloneQualifier(cell)) + ", " + Bytes.toString(CellUtil.cloneValue(cell))
                    );
                }
            }
            table.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
    
    /**
     * 扫描表
     * @param tableName
     * @param cf
     * @param cn
     */
    public void scanner(String tableName, String cf, String cn){
        try {
            Table table = connection.getTable(TableName.valueOf(tableName));
            Scan scan = new Scan();
            scan.setMaxVersions(3);     // 最大版本号
//            scan.addFamily(Bytes.toBytes(cf));
            scan.addColumn(Bytes.toBytes(cf), Bytes.toBytes(cn));
            ResultScanner scanner = table.getScanner(scan);
            for (Result result: scanner) {
                Cell[] cells = result.rawCells();
                for (Cell cell: cells) {
                    System.out.println(Bytes.toString(CellUtil.cloneRow(cell)) + ", " + Bytes.toString(CellUtil.cloneFamily(cell)) + ", "
                            + Bytes.toString(CellUtil.cloneQualifier(cell)) + ", " + Bytes.toString(CellUtil.cloneValue(cell))
                    );
                }
            }
            table.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
    

```
### 7. 删除数据
```
    /**
     * 删除数据
     * @param tableName
     * @param cf
     * @param cn
     * @param rowKey
     */
    public void delete(String tableName, String cf, String cn, String rowKey){
        try {
            Table table = connection.getTable(TableName.valueOf(tableName));
            // 只指定rowkey 是删除的row下所有的版本号数据
            Delete delete = new Delete(Bytes.toBytes(rowKey));
            // 如果指定列, 列祖, 删除的是最高的版本数据 
            delete.addColumn(Bytes.toBytes(cf), Bytes.toBytes(cn));     // 
            table.delete(delete);
            table.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
    /**
     * 删除多条数据
     * 
     * @param tableName
     * @param cf
     * @param cn
     * @param rowKeys
     */
    public void delete(String tableName, String cf, String cn, String... rowKeys){
        try {
            Table table = connection.getTable(TableName.valueOf(tableName));
            List<Delete> dels = new ArrayList<>();
            for (String rowKey : rowKeys) {
                Delete delete = new Delete(Bytes.toBytes(rowKey));
                delete.addColumn(Bytes.toBytes(cf), Bytes.toBytes(cn));
            }
            table.delete(dels);
            table.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    
```


### 8. HBase与MR
```
官方HBase-MapReduce
1．查看HBase的MapReduce任务的执行
$ bin/hbase mapredcp

2．环境变量的导入
（1）执行环境变量的导入（临时生效，在命令行执行下述操作）
$ export HBASE_HOME=/opt/module/hbase-1.3.1
$ export HADOOP_HOME=/opt/module/hadoop-2.7.2
$ export HADOOP_CLASSPATH=`${HBASE_HOME}/bin/hbase mapredcp`

（2）永久生效：在/etc/profile配置
export HBASE_HOME=/opt/module/hbase-1.3.1
export HADOOP_HOME=/opt/module/hadoop-2.7.2
并在hadoop-env.sh中配置：（注意：在for循环之后配）, scp分发到其他机器上, 未配置会报classNotFindException
export HADOOP_CLASSPATH=$HADOOP_CLASSPATH:/opt/module/hbase/lib/*

3．运行官方的MapReduce任务
案例一：统计Student表中有多少行数据
$ /opt/module/hadoop-2.7.2/bin/yarn jar lib/hbase-server-1.3.1.jar rowcounter student

案例二：使用MapReduce将本地数据导入到HBase
1）在本地创建一个tsv格式的文件：fruit.tsv
1001	Apple	Red
1002	Pear		Yellow
1003	Pineapple	Yellow

2）创建HBase表
hbase(main):001:0> create 'fruit','info'

3）在HDFS中创建input_fruit文件夹并上传fruit.tsv文件
$ /opt/module/hadoop-2.7.2/bin/hdfs dfs -mkdir /input_fruit/
$ /opt/module/hadoop-2.7.2/bin/hdfs dfs -put fruit.tsv /input_fruit/

执行MapReduce到HBase的fruit表中
$ /opt/module/hadoop-2.7.2/bin/yarn jar lib/hbase-server-1.3.1.jar importtsv \
-Dimporttsv.columns=HBASE_ROW_KEY,info:name,info:color fruit \
hdfs://hadoop102:9000/input_fruit

使用scan命令查看导入后的结果
hbase(main):001:0> scan ‘fruit’

```


