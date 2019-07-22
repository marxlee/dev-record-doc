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
