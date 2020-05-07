# spark-streaming

## 自定义接受器

```
import java.io.{BufferedReader, InputStreamReader}
import java.net.Socket

import org.apache.spark.storage.StorageLevel
import org.apache.spark.streaming.receiver.Receiver
/**
*   继承Receiver[泛型](保存位置)
*
*/
class CustomerReceiver(host:String, port:Integer) extends Receiver[String](StorageLevel.MEMORY_ONLY){

  def receiver(): Unit = {
    var socket:Socket = null
    try {
      socket = new Socket(host, port)
      val read = new BufferedReader(new InputStreamReader(socket.getInputStream))
      var str = read.readLine()
      while (!isStopped() && str != null){
        store(str)
        str = read.readLine()
      }
      // 执行上述函数过程后 重启
      restart("restart")

    }catch {
        case e:Exception => restart("restart")

    }
  }

  // 重写 onStart
  override def onStart(): Unit = {

    new Thread("receiver"){
      override def run(): Unit = {
        receiver()
      }
    }.start()

  }

  // 重写 onStop方法
  override def onStop(): Unit = {

  }
}
```

```
import org.apache.spark.SparkConf
import org.apache.spark.streaming.{Seconds, StreamingContext}

object SparkStreaming {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("ssc").setMaster("local[*]")

    val ssc = new StreamingContext(conf, Seconds(5))

    val lineDstream = ssc.receiverStream(new CustomerReceiver("hadoop107", 9999))
    val fmDS = lineDstream.flatMap(_.split(" "))

    val k_vDS = fmDS.map((_, 1))
    val kvRdds = k_vDS.reduceByKey(_+_)
    kvRdds.print()

    ssc.start()
    ssc.awaitTermination()


  }

}
```




## 转换
Dstream 转换 -> 有状态 -> 无状态转换

### 有状态转换
1. 有状态依赖checkpoint("./checkpoint")  
2. 其目的是为了保存上一次计算结果的值, 数据流进入下一次执行操作时, 会将上一次计算结果加到当前计算结果上, 在保存到checkpoint中, 依次执行  
3. 执行 : dstream.updateStateByKey[S: ClassTag](updateFunc: (Seq[V], Option[S]) => Option[S])  
4. 如果checkpoint未指定, error: The checkpoint dirctory is not set

```
import org.apache.spark.SparkConf
import org.apache.spark.streaming.{Seconds, StreamingContext}

object SparkStreaming2 {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("ssc").setMaster("local[*]")

    val ssc = new StreamingContext(conf, Seconds(5))

    ssc.checkpoint("./sstest-checkpoint")
    val lineDstream = ssc.receiverStream(new CustomerReceiver("hadoop107", 9999))
    val fmDS = lineDstream.flatMap(_.split(" "))

    val k_vDS = fmDS.map((_, 1))
//    val kvRdds = k_vDS.reduceByKey(_+_)
//    kvRdds.print()

    // 自定义使用checkpoint
    val kvRdds = k_vDS.updateStateByKey((v:Seq[Int], o:Option[Int])=>{
      val ov = o.getOrElse(0)
      val s = v.sum + ov
      Some(s)
    })
    kvRdds.print()

      // 设置重复数据去重
//    val result = k_vDS.reduceByKeyAndWindow((x:Int, y:Int) => x + y,(a:Int, b:Int)=>a-b, Seconds(10), Seconds(5))
//    result.print()
      
      // 不设置重复数据
//    val result = k_vDS.reduceByKeyAndWindow((x:Int, y:Int) => x + y, Seconds(10), Seconds(5))
//    result.print()

    ssc.start()
    ssc.awaitTermination()


  }
}

```
### window-operation
1. window-operation 窗口滑块(窗口大小, 步长)  
2. 窗口大小: 时间维度  
3. 步长: 时间维度  
4. 窗口大小应该是步长大小的倍数  

```
 /**
   * Return a new DStream by applying `reduceByKey` over a sliding window. This is similar to
   * `DStream.reduceByKey()` but applies it over a sliding window. Hash partitioning is used to
   * generate the RDDs with Spark's default number of partitions.
   * @param reduceFunc associative and commutative reduce function
   * @param windowDuration width of the window; must be a multiple of this DStream's
   *                       batching interval
   * @param slideDuration  sliding interval of the window (i.e., the interval after which
   *                       the new DStream will generate RDDs); must be a multiple of this
   *                       DStream's batching interval
   */

  def reduceByKeyAndWindow(
      reduceFunc: (V, V) => V,
      windowDuration: Duration,
      slideDuration: Duration
    ): DStream[(K, V)] = ssc.withScope {
    reduceByKeyAndWindow(reduceFunc, windowDuration, slideDuration, defaultPartitioner())
  }
  
  
   /**
   * Return a new DStream by applying incremental `reduceByKey` over a sliding window.
   * The reduced value of over a new window is calculated using the old window's reduced value :
   *  1. reduce the new values that entered the window (e.g., adding new counts)
   *
   *  2. "inverse reduce" the old values that left the window (e.g., subtracting old counts)
   *
   * This is more efficient than reduceByKeyAndWindow without "inverse reduce" function.
   * However, it is applicable to only "invertible reduce functions".
   * Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
   * @param reduceFunc associative and commutative reduce function "统计数据结果"
   * @param invReduceFunc inverse reduce function; such that for all y, invertible x:
   *                      `invReduceFunc(reduceFunc(x, y), x) = y` "去重操作"
   * @param windowDuration width of the window; must be a multiple of this DStream's
   *                       batching interval
   * @param slideDuration  sliding interval of the window (i.e., the interval after which
   *                       the new DStream will generate RDDs); must be a multiple of this
   *                       DStream's batching interval
   * @param filterFunc     Optional function to filter expired key-value pairs;
   *                       only pairs that satisfy the function are retained
   */
  def reduceByKeyAndWindow(
      reduceFunc: (V, V) => V,
      invReduceFunc: (V, V) => V,
      windowDuration: Duration,
      slideDuration: Duration = self.slideDuration,
      numPartitions: Int = ssc.sc.defaultParallelism,
      filterFunc: ((K, V)) => Boolean = null
    ): DStream[(K, V)] = ssc.withScope {
    reduceByKeyAndWindow(
      reduceFunc, invReduceFunc, windowDuration,
      slideDuration, defaultPartitioner(numPartitions), filterFunc
    )
  }
  
// 设置规则窗口大小是步长的倍数 
rddDStream.reduceByKeyAndWindow((x:Int, y:Int) => x + y,(a:Int, b:Int)=>a-b, Seconds(10), Seconds(5)) 
  
```






