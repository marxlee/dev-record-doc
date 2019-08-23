# numpy
```
import numpy as np
import random


# 生成数组
a1 = np.array([[1,2,3]])
print(a1)
print(a1.shape)

# 重新设置形状 3 * 1 = 3 数据总数,
r1 = a1.reshape((3, 1))
print(r1)
print(r1.shape)

# 计算尾部二维数据, 对应位置值相同, 或者有一个为1 : (3, 1) + (1, 3)
print(r1 + a1)

# 设置dtype
a2 = np.array(range(0,4), dtype=float)

print(a2)
print(a2.dtype)

# bool
a3 = np.array([0, 1, 1], dtype=bool)
print(a3)
print(a3.dtype)

ar3 = a3.astype(dtype='i8')
print(ar3)

# 随机生成小数
a4 = np.array([random.random() for i in range(10)])
print(a4)

# 轴(axis) 二维: 0=行  1=列

# numpy读取数据
teams = np.loadtxt("./data/data1.txt", delimiter=',')
print(teams)
# 转换
rt = teams.reshape((teams.shape[1], teams.shape[0]))
print(rt)
# 转至行列式
teams1 = np.loadtxt("./data/data1.txt", delimiter=',', unpack=True)
print(teams1)
tt1 = teams1.transpose()
print(tt1)
tt1.swapaxes(1, 0)
print(tt1.T)

# numpy索引切片

print(tt1[1, 1])

# 连续多行
print(tt1[2:])

# 不连续多行
print(tt1[[0, 2]])

# 列
print(tt1[:, 0])
# 不连续
print(tt1[:, [0, 3]])

print(tt1[2, 2:])

# 条件取值 + 替换
tt1[tt1 < 3] = 0
print(tt1)

tt1 = np.where(tt1 <= 1, 2.6, 8)
print(tt1)

print(tt1.clip(5, 8))

# 赋值nan 必须是浮点型float类型
tt1[2, 3] = np.NAN
print(tt1)

# 拼接
# 数值拼接
vs = np.vstack((teams, tt1))
print(vs)
# 水平拼接
hs = np.hstack((teams, tt1))
print(hs)

# 行列交换
# 行交换
vs1 = vs[[0, 2], :] = vs[[2, 0], :]
print(vs)

# 列交换
vs[:, [2, 0]] = vs[:, [0, 2]]
print(vs)

# 创建一个全为 0 的数组 n 行一列
zeros = np.zeros([vs.shape[0], 1])
print(zeros)

# 方阵
eyes = np.eye(3)
print(eyes)










```
