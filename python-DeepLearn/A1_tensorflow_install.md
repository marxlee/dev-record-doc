##  安装anaconda 3.7

```
python --version

# pip版本
pip --version
# 需要升级pip
pip install --upgrade pip
# 如果pip显示未安装, 执行以下命令
easy_install pip
  

virtualenv --version

pip install -U pip virtualenv

# 安装到用户文件下, 不过安装过程中会有警告, 没关系, 也可以不适用 --user
pip install --user --upgrade tensorflow  # install in $HOME

# 注意, 这个版本安装的是1.4版本, 如果python 版本过低的情况下, 是不能安装成功的
# 执行以下命令, 成功会返回数据 Tensor<....>
python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

```

