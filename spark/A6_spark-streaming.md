# spark-streaming

## 转换
Dstream 转换 -> 有状态 -> 无状态转换

### 有状态转换
1. 有状态依赖checkpoint("./checkpoint")  
2. 其目的是为了保存上一次计算结果的值, 数据流进入下一次执行操作时, 会将上一次计算结果加到当前计算结果上, 在保存到checkpoint中, 依次执行  
3. 执行 : dstream.updateStateByKey[S: ClassTag](updateFunc: (Seq[V], Option[S]) => Option[S])  
4. 如果checkpoint未指定, error: The checkpoint dirctory is not set

