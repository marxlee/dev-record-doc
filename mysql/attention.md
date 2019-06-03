## 解决1: mysql表数据插入异常 原因, 数据结构错误
```
MYSQL: Caused by: java.sql.SQLException: Incorrect string value: '\xF0\x9F\x98\x80\xE3\x80...' for column 'show_content' at row 1

# 将数据表结构改为utf8mb4 格式, 防止数据在插入的时候
> ALTER TABLE TABLE_NAME CONVERT TO CHARACTER SET utf8mb4;

```
