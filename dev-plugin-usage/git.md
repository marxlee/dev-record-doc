
# Git command

### Git 常用命令
```
# 初始化文件目录(新建仓库)
git init

# 添加文件到缓冲区
git add <file>

# 提交本地仓库
git commit -m "first commit"

# 推送远程仓库指定分支
git push -u origin master

# 查看缓存区状态: 添加到缓存区的文件和未添加到缓存区的文件
git status

### 显示所有远程分支
git branch -a 

# 显示本地分支目录
git branch --list

# 回滚到指定提交日志
git reset --hard <uid>
# 回退到上一个版本
git reset --hard HEAD

# 删除缓存区文件
git reset HEAD <file>


# 添加一个远程仓库
git remote add origin https://github.com/marxlee/Development-doc.git
```

### Git 大文件操作
```
1. 先安装 git-lfs
brew install git-lfs
2. git 内部安装
git lfs install
3. 追踪文件后缀: 也可以是指定文件, 或者文件后缀
git lfs track "*.psd"
4. 提交到缓冲区
git add .gitattributes
```



