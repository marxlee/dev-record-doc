## Simplify Operation: 基本操作
```
1．进入HBase客户端命令行
[hadoop102 hbase]$ bin/hbase shell

2．查看帮助命令
hbase(main):001:0> help

3．查看当前数据库中有哪些表
hbase(main):002:0> list
```

## 表的操作
```
1．创建表
hbase(main):002:0> create 'student','info'

2．插入数据到表
hbase(main):003:0> put 'student','1001','info:sex','male'
hbase(main):004:0> put 'student','1001','info:age','18'
hbase(main):005:0> put 'student','1002','info:name','Janna'
hbase(main):006:0> put 'student','1002','info:sex','female'
hbase(main):007:0> put 'student','1002','info:age','20'

3．扫描查看表数据
hbase(main):008:0> scan 'student'
hbase(main):009:0> scan 'student',{STARTROW => '1001', STOPROW  => '1001'}
hbase(main):010:0> scan 'student',{STARTROW => '1001'}

4．查看表结构
hbase(main):011:0> describe ‘student’

5．更新指定字段的数据
hbase(main):012:0> put 'student','1001','info:name','Nick'
hbase(main):013:0> put 'student','1001','info:age','100'

6．查看“指定行”或“指定列族:列”的数据
hbase(main):014:0> get 'student','1001'
hbase(main):015:0> get 'student','1001','info:name'

7．统计表数据行数
hbase(main):021:0> count 'student'

8．删除数据
删除某rowkey的全部数据：
hbase(main):016:0> deleteall 'student','1001'
删除某rowkey的某一列数据：
hbase(main):017:0> delete 'student','1002','info:sex'
删除时间戳的数据: 删除规则: 删除时间戳之前的所有版本号数据, 保留这个时间戳后边的数据
hbase(main):017:0> delete 'student','1002','info:sex', 1503343423402

9．清空表数据
hbase(main):018:0> truncate 'student'
提示：清空表的操作顺序为先disable，然后再truncate。

10．删除表
首先需要先让该表为disable状态：
hbase(main):019:0> disable 'student'
然后才能drop这个表：
hbase(main):020:0> drop 'student'
提示：如果直接drop表，会报错：ERROR: Table student is enabled. Disable it first.

11．变更表信息
将info列族中的数据存放3个版本：
hbase(main):022:0> alter 'student',{NAME=>'info',VERSIONS=>3}
hbase(main):022:0> get 'student','1001',{COLUMN=>'info:name',VERSIONS=>3}

12 命名空间的使用
默认情况下, 在创建表的时候, 是不需要加命名空间的, 默认情况下使用的是 default命名空间, 也就是RegionServer Group 
hbase(main):022:0>create_namespace 'group_product'
hbase(main):022:0>list_namespace
hbase(main):022:0>create 'group_product:pro', 'cf1'

# 删除命名空间: 必须删除 disable, drop 命名空间下所有的表
hbase(main):022:0>disable 'group_product:pro'
hbase(main):022:0>drop 'group_product:pro'
hbase(main):022:0>drop_namespace 'group_product' 
hbase(main):022:0>

```


