## 查找mysql/mariadb
$ rpm -qa | grep mysql

$ rpm -qa | grep mariadb

## 删除mysql/mariadb
#### 1. 普通删除模式
$ rpm -e mysql

$ rpm -e mariadb

#### 2. 强力删除模式，如果使用上面命令删除时，提示有依赖的其它文件，则用该命令可以对其进行强力删除
$ rpm -e --nodeps mysql

$ rpm -e --nodeps mariadb

## 下面安装mariadb
$ yum install mariadb-server mariadb 

## 更新mariadb-service, 找不到mysql命令
$ yum install -y mariadb-server

## 结束后清理yum
$ yum clean all

## 启动, 停止, 开机启动
$ systemctl start mariadb.service  #启动MariaDB

$ systemctl stop mariadb  #停止MariaDB

$ systemctl restart mariadb  #重启MariaDB

$ systemctl enable mariadb  #设置开机启动

## 查阅版本号
$ mysqladmin --version

## 设置新密码
$ mysqladmin -u root password "root";

## 登录mariaDB(可以使用mysql)
$ mysql -u root -p root

## 创建新的用户
```
show databases;
use mysql;
insert into mysql.user(Host,User,Password) values('localhost','hadoop',password('hadoop'));
```

## 添加用户访问权限
```
1. > GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'root' WITH GRANT OPTION;
2. > GRANT ALL PRIVILEGES ON *.* TO 'hadoop'@'%' IDENTIFIED BY 'hadoop' WITH GRANT OPTION;
3. > flush privileges;
```


### JDBC驱动
org.mariadb.jdbc.Driver

### Java连接方式
jdbc:mariadb://localhost:3306/DB?user=root&password=myPassword


