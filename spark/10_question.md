# 常见问题分析和解决

### 读取本地和hdfs文件
```
// 当集群模式配置到hadoop的hdfs上时, 需要读取本地文件, 可以使用file:///模式读取
sc.textFile("file:///Readme.txt")
// 默认情况是, 如果不加file:// 会默认读取 hadoop:9000/的目录下的文件
sc.textFile("/Readme.txt")

```

