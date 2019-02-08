### GOPATH设置:
`$ vi ~/.bash_profile `


```
## go 安装路径
export GOROOT='/usr/local/go'
## 处理器
export GOARCH='amd64'
## 系统
export GOOS='darwin'
## gopath路径
export GOPATH='/Users/libinbin/tmp/gopath'
## 添加到path
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin
## '/bin:/sbin:/usr/bin:/usr/local/bin:/usr/local/go/bin'
```



1. 在%GOPATH%\src\ 目录下，建立golang.org 文件夹，并再新建x文件夹。  目录为 "%GOPATH\src\golang.org\x\"

2. 完成目录切换后，开始下载插件包：
`$ git clone https://github.com/golang/tools.git tools`

3. 执行完以后，会多一个tools文件夹。

4. 打开vsCode终端，切换到 终端，进入“%GOPATH”目录,执行

[原文引用](https://blog.csdn.net/yo_oygo/article/details/79065966)

```
go install golang.org/x/tools/cmd/gorename
go install github.com/josharian/impl
go install github.com/rogpeppe/godef
go install github.com/sqs/goreturns
go install github.com/golang/lint/golint
go install github.com/cweill/gotests/gotests
```


5. 单独处理golint : golint的源码位于https://github.com/golang/lint

```
# 进入目录
$ cd %GOPATH%\src\golang.org\x
## 下载golint需要的源码
$ git clone https://github.com/golang/lint 
## 进入到%GOPATH%下，执行
$ go install github.com/golang/lint/golint
```

### 这样，vscode的golang插件所依赖的工具安装完成了。

[原文引用](https://blog.csdn.net/bing2011/article/details/81183569)

