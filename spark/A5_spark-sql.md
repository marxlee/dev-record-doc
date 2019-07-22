# spark sql (session)



rdd  data frame data set

jvm 内存, + 定制化内存  性能比rdd高

懒执行

优化执行方法


frame 类型检查

set   f的特殊形式

```
--RDD ->DF/DS
	--DF:
		--rdd.map{x=> val pa=x.split(",");(pa(0).trim,pa(1).trim)}.toDF("name","age")
		--case class People(name:String,age:String)
		rdd.map{x=> val pa=x.split(",");People(pa(0).trim,pa(1).trim)}.toDF
		--

	--DS:case class People(name:String,age:String)
		rdd.map{x=> val pa=x.split(",");People(pa(0).trim,pa(1).trim)}.toDS

--DF  ->RDD/DS
	--RDD DF.rdd,获取值，编译器不校验类型
	--case class People(name:String,age:String)
		DF.as[People]

--DS  ->RDD/DF
	--RDD DS.rdd，获取值，编译器校验类型
	--DS.toDF
  
  DF = DS[row]
```

1. sql 是什么
spark 管理结构化的模块

2. 关键抽象是什么
RDD(1.0) DataFrame(1.3) DataSet(1.6)
rdd 行处理

dataFrame 列信息处理, 

dataset 列式处理, 列加了类型处理

DataFrame api的扩展
spark最新的数据抽象
具有类型安全检查
具有dataFrame插询优化特性
DataSet支持编解码器
样例类的使用
DataFrame=DataSet[row]
DataSet是强类型


3. sql 操作
相互转化: 


4. sql-udf

5. sql数据源

6. 实战







