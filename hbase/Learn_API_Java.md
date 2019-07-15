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





