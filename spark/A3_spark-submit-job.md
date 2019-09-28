

## 提交过程

1、通过Jar包提交任务【工作中的主要方式】

1、需要通过bin/spark-submit来提交
2、【必需】--class 指定你jar包的主类
3、【必需】--master 指定你访问的集群地址  如果你的jar包中已经配置了master，那么可以不指定master地址。
4、【必需】你的jar包的具体路径。 jar的参数
5、通过  bin/spark-submit 可以看到所有的参数：


2、如何通过IDEA编写spark应用程序
    1、创建一个scala文件
    2、创建一个 sparkConf对象，设置应用的名称，【可选】设置master地址
    3、通过sparkConf创建 sparkContext【用于连接spark的桥梁】
    4、编写业务逻辑
    5、关系sparkContext， sc.stop()

3、如果你使用bin/spark-shell 那么sparkContext默认为 sc
4、IDEA打包spark应用的时候，不需要讲spark的jar包和scala的jar包打入到jar包中，运行环境中都有。
5、来开发过程中，可以通过local[*]模式来运行，并调试。

6、所有的提交方式



7、deploy-mode  client模式和cluster模式

client模式：一般用在测试过程中，Driver运行在client的主机上。一般会等待整个程序的执行完成。
cluster模式： 一般是生产环境中，Client在提交Jar包之后，退出，不等待整个应用程序的执行，Driver会运行在某一个worker上。


## IDEA环境应用
spark shell仅在测试和验证我们的程序时使用的较多，在生产环境中，通常会在IDE中编制程序，然后打成jar包，然后提交到集群，最常用的是创建一个Maven项目，利用Maven来管理jar包的依赖。
### 在IDEA中编写WordCount程序
1）创建一个Maven项目WordCount并导入依赖
```
<dependencies>
    <dependency>
        <groupId>org.apache.spark</groupId>
        <artifactId>spark-core_2.11</artifactId>
        <version>2.1.1</version>
    </dependency>
</dependencies>
<build>
        <finalName>WordCount</finalName>
        <plugins>
            <plugin>
                <groupId>net.alchim31.maven</groupId>
                <artifactId>scala-maven-plugin</artifactId>
                <version>3.2.2</version>
                <executions>
                    <execution>
                        <goals>
                            <goal>compile</goal>
                            <goal>testCompile</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-assembly-plugin</artifactId>
                <version>3.0.0</version>
                <configuration>
                    <archive>
                        <manifest>
                            <mainClass>WordCount(修改)</mainClass>
                        </manifest>
                    </archive>
                    <descriptorRefs>
                        <descriptorRef>jar-with-dependencies</descriptorRef>
                    </descriptorRefs>
                </configuration>
                <executions>
                    <execution>
                        <id>make-assembly</id>
                        <phase>package</phase>
                        <goals>
                            <goal>single</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
</build>
```
2）编写代码
```
package com.xxxX

import org.apache.spark.{SparkConf, SparkContext}

object WordCount{

  def main(args: Array[String]): Unit = {

//创建SparkConf并设置App名称
    val conf = new SparkConf().setAppName("WC")

//创建SparkContext，该对象是提交Spark App的入口
    val sc = new SparkContext(conf)

    //使用sc创建RDD并执行相应的transformation和action
    sc.textFile(args(0)).flatMap(_.split(" ")).map((_, 1)).reduceByKey(_+_, 1).sortBy(_._2, false).saveAsTextFile(args(1))

    sc.stop()
  }
}
```
3）打包到集群测试
```
bin/spark-submit \
--class WordCount \
--master spark://hadoop102:7077 \
WordCount.jar \
/word.txt \
/out
```


