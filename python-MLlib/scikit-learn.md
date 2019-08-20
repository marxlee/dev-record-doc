# 特征

# tf-idf 特征抽取

# 图片
特征(行) + 样本(列)

数据特征预处理
1. 通过特定的统计方法(数学方法), 将数据转换成算法要求的数据
	1. 数值型数据: 标准缩放: 
					1. 归一化
					2. 标准化
					3. 缺市值

		1. 归一化: 
			1).对原始数据进行变化, 将数据映射到[0,1]之间
			X` = (x - min)/ (max -min),  X``= X`(mx - mi) + mi 
			x=当前值, max=列最大值, min=列最小值, mx mi=设定的最大值最小值[1, 0], X`=计算结果, X``=计算结果

			2) 缺点: 针对异常点过大, 过多的情况, 鲁棒性较差, 使用于传统小场景
			api: sklearn.preprocessing.MinMaxScaler

		2. 标准化: 
			1) 公式: X` = x - mean/σ , mean=平均值, σ=标准差 
			σ = √var = √ ( (x1 - mean)2 + (x2 - mean)2+.../n(特征样本数量) )  var=方差值
			
			2) 将数据转化为 平均值为0, 标准差为1的范围内的数据

			3) api:  proprocessing.standardScaler

			4) 适合大数据场景下, 比较稳定的场景


		3. 缺失值: 
			pandas
			处理: 删除, * 填充 (按列(特征)填补) *

	2. 类别行: one-hot类型

	3. 时间类型: 时间切分



# 数据降维: 特征的数量(减少列)
	1. 特征选择
	2. 主成分分析

	1. 特征选择: 
		1) 是什么: 冗余: 部分数据相关度高, 影响数据分析, 噪音: 
			1. 过滤式: filter -> VarianceThreshold  	***
			2. 嵌入式: Embedded -> 正则化, 决策树 		***
			3. 包裹式: Wrapper
		2) api	feature_selection.VarianceThrashold.fit_transform([[],[]])
		3) 
	

	2. 主成分分析:
		PCA 分析简化数据技术
		特征数量达到 上百个 的时候, 考虑数据特征的简化, 使用pca, 特征数量减少, 同时数据也会改变. 
		n_components: 小数 (0-1: 信息保留量90%-95%) *** 
					  整数 (减少到的特征数量)


		API: decomposition.PCA.fit_transform() 


算法: 
	数据类型: 离散型, 连续性数据

	监督学习: (预测) 特征 + 目标 -> 预测男女
		分类(离散): k-临近算法, 贝叶斯算法, 决策树于随机森林, 逻辑回归, 神经网络
			二分类问题
		回归(连续): 线性回归, 岭回归

	无监督学习 : 特征  -> 
		聚类: k-means



数据分析流程: 
	数据, 训练模型, 评估(训练集, 测试集)(70, 30)(80, 20)
		x_train, y_train, x_test, y_test



	数据划分: 
		API: 
		数据划分: sklearn.model_selection.train_test_split
		分类数据: datasets:
			1. datasets.load_*()
				小规模数据获取
			2. datasets.fetch_*(data_home=None)
				网络获取, data_home是下载到的文件目录, 默认~/scikit_learn-data/ 
			3. datasets.load_iris()
			4. fetch_20newsgroups(data_home=None, subset='train')
				subset: train, test, all 
			5. datasets.clear_data_home(data_home=None)

		回归数据: 波士顿房价信息
			datasets.load_boston()

转换器: 


估计器: (评估算法的api)
	estimator: 
		1. predict(x_test) 预测
		2. score(x_test, y_test) 预测的准确率



算法: 
	分类算法: (目标是离散数据)
		两个样本之间的距离, 未知点 -> 已知点 a -> b 相似点, 距离相近
		k-近邻算法: KNN 
		a(a1, a2, a3) b(b1, b2, b3)

		欧式距离算法 = √( (a1 -b1)2 + (a2 - b2)2 + (a3 -b3)2 )

		API:	
			sklearn.neighbors.KNeighborsClassifer(n_neighbors=5, algorithm='auto')
			n_..: int 默认5 插询默认使用邻近数(个数), 会影响结果
			al..: {'auto', 'ball_tree', 'kd_tree', 'brute'}, 算法选择, auto会根据传入的fit决定使用不同的算法(不同算法影响效率)



		数据预处理: 
			1. 首先需要数据标准化 
			2. sklearn,  axis=1 列 pandas axis=0列
      

2. 朴素贝叶斯分类
概念: 寻找一个目标的概率, 特征条件相互独立

应用: 文档分类
	文档: 词1, 词2, 词3,.... 词9, 词10....
	P(科技\|文档)
	P(娱乐\|文档) 
	P(科技\|词1, 词2....[特征])
	P(娱乐\|词1, 词2....[特征]) 
	
	

条件概率: 事件A在另外一种事件B已经发生的条件是的发生概率
	P(A|B)
	P(A1,A2|B) = P(A1|B) \* P(A2|B)
	A1, A2 条件相互独立
联合概率: 包含多个条件, 切所有条件同时成立的概率
	P(a1, a2) = P(a1) \* P(a2)
	

公式: 
P(C\|W) = (P(W\|C)P(C))/P(W)
	W:给定文档的特征值(频数统计, 预测文档提供)
	C:文档类别

P(C\|F1,F2,....) = ( P(F1,F2,....\|C)P(C) ) / P(F1,F2,....)
公式: 
  1. P(C): 每个文档类别的概率(某文档类别数 \/ 总文档数量)
  2. P(W\|C): 给定类别下的特征(被预测文档的出现的词)的概率
    计算方法: P(F1\|C) = Ni \/ N
    Ni为F1词在C类别所有文档中出现的次数
    N为所属类别下C下的文档所有词出现的次数和
  3. P(F1,F2....) 预测文档中每个词的概率
  
  
  拉普拉斯平滑系数:  防止数值为 0 
  P(W\|C) = (Ni+a) / (N+am)
  a: 值为指定的系数一般为1, m为训练文章统计出来的特征词个数
  
  API: sklearn.naive_bayes.MultinomialNB(alpha=1.0)
  alpha: 拉普拉斯平滑系数
  
缺点: 
数据误差大结果受影响
对于假设性的文章, 会对结果造成干扰

神经网络的效果是比贝叶斯算法是好一些的


结果优点: 
不需要调参, 算法简单, 对数据缺失不明感



混淆矩阵: 
  预测结果与正确结果, 存在四中不同的组合, 构成混淆矩阵, 适合多分类
  
  预测结果: 
  横向: 预测结果, 纵向为真是结果
  
|  |正例|返例|
|:--:|:--:|:--:|
|正例|真正例|伪反例|
|反例|伪正例|真反例|

准确率和召回率

召回率: F1_score, 反应模型的稳健性

分类评估分析:
API: sklearn.metrics.classification_report(x_true, y_pred, target_names=None)
x_true: 真实目标值
y_pred: 估计器预测目标值
target_names: 目标类别名称
return 每个类别准确率和召回率


交叉验证: 
将所有数据等分N等分



	
