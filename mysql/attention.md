## 解决1: mysql表数据插入异常 原因, 数据结构错误
```
MYSQL: Caused by: java.sql.SQLException: Incorrect string value: '\xF0\x9F\x98\x80\xE3\x80...' for column 'show_content' at row 1

# 将数据表结构改为utf8mb4 格式, 防止数据在插入的时候
> ALTER TABLE TABLE_NAME CONVERT TO CHARACTER SET utf8mb4;

# 更新自己的表内的操作
update a t1  join b t2 on t1.id=t2.id set t1.name=t2.name where t1.id=2016;

# 修改字段长度命令
alter table 表名 modify column 列名 类型(要修改的长度);
alter table bank_branch_number modify column bankId varchar(10);

# 添加一个表的字段
alter table `表名` add `字段` varchar(50) default null comment "注释";

```
