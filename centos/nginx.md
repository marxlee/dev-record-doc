# nginx 安装 root 用户权限下进行安装

## 第一种 yum 源安装
```
# 要添加CentOS 7 EPEL仓库，请打开终端并使用以下命令：
yum install epel-release
# 第二步 - 安装Nginx
# 在对提示回答yes后，Nginx将在服务器上完成安装。
sudo yum install nginx
# 第三步 - 启动Nginx
sudo systemctl start nginx
# 当然, 由此安装的nginx的配
1. 页面会有所提示: nginx的安装目录: /usr/local/nginx
2. 页面会提示nginx的配置文件的路径: /etc/nginx/nginx.conf
# 关闭nginx
systemctl stop nginx

```

### 修改配置文件nginx.conf文件, 添加代理, nginx添加负载均衡为
```
http {
    include       mime.types;
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #服务器的集群  
    upstream  yournet.com {  
      #服务器集群名字   
      #服务器配置   weight是权重的意思，权重越大，分配的概率越大。
      #server    127.0.0.1:18080;  
      #server    127.0.0.1:28080; 
      server    192.168.10.200:18080; 
      server    192.168.10.200:28080; 
 
    }   
    server {
        listen       80;
        server_name  localhost;
        
        // 当前位置添加代理负载均衡
	      location / {
            proxy_pass http://yournet.com;
            proxy_redirect default;
        }


        #error_page  404      /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }
} 

# 重启nginx
systemctl restart nginx.service

# 查看nginx进程
ps -ef | grep nginx

```

# 第二种软件包安装
```
安装运行环境: 
Nginx是C语言开发,建议在linux上运行,本教程使用Centos7.0作为安装环境.
1)gcc
安装nginx需要先将官网下载的源码进行编译，编译依赖gcc环境，如果没有gcc环境，需要安装gcc
需要执行的命令:yum install gcc-c++ 
2)PCRE
PCRE(Perl Compatible Regular Expressions)是一个Perl库，包括 perl 兼容的正则表达式库。nginx的http模块使用pcre来解析正则表达式，所以需要在linux上安装pcre库。
需要执行的命令:yum install -y pcre pcre-devel
3)zlib
zlib库提供了很多种压缩和解压缩的方式，nginx使用zlib对http包的内容进行gzip，所以需要在linux上安装zlib库。
需要运行的命令:yum install -y zlib zlib-devel
4)openssl
OpenSSL 是一个强大的安全套接字层密码库，囊括主要的密码算法、常用的密钥和证书封装管理功能及SSL协议，并提供丰富的应用程序供测试或其它目的使用。
nginx不仅支持http协议，还支持https（即在ssl协议上传输http），所以需要在linux安装openssl库。
需要运行的命令:yum install -y openssl openssl-devel

2)配置configure:
在nginx-1.8.0目录下运行如下命令:


> ./configure \  
--prefix=/usr/local/nginx \  
--pid-path=/var/run/nginx/nginx.pid \  
--lock-path=/var/lock/nginx.lock \  
--error-log-path=/var/log/nginx/error.log \  
--http-log-path=/var/log/nginx/access.log \  
--with-http_gzip_static_module \  
--http-client-body-temp-path=/var/temp/nginx/client \  
--http-proxy-temp-path=/var/temp/nginx/proxy \  
--http-fastcgi-temp-path=/var/temp/nginx/fastcgi \  
--http-uwsgi-temp-path=/var/temp/nginx/uwsgi \  
--http-scgi-temp-path=/var/temp/nginx/scgi</span></strong>  


3)编译安装

执行make命令
执行make stall命令

4)运行Nginx

进入到sbin目录下,执行./nginx命令.


5)查看进程

安装成功查看安装目录

3.测试Nginx是否运行成功
Nginx的端口是80,所以在浏览器上运行http:[linux的ip地址]即可,如果运行成功,出现如下界面


如果没有出现下面的界面,表示远程连接没有成功,如果linux的进程已经启动,尝试着将linux的防火墙关闭,运行如下命令,关闭防火墙,然后查看一下防火墙的状态.

执行完这个操作以后,再查看一下在本地是否能连上Nginx.
遇到的问题:
1.[emerg]mkdir()"/var/temp/nginx/client" failed(2:No such file or directory)

解决方法:
查看了一下是由于没有Nginx/client的目录.缺少对应的文件,建立相应的文件就好.
2.nginx/logs/nginx.pid" failed (2: No such file or directory)


解决方法:
重新编译(make,make install),安装就好.


```


