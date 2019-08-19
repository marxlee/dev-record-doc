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
      






