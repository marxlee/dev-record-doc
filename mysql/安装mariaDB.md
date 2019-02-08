## 查找mysql/mariadb(类似)
$ rpm -qa | grep mysql


$ rpm -e mysql　　// 普通删除模式
$ rpm -e --nodeps mysql　　// 强力删除模式，如果使用上面命令删除时，提示有依赖的其它文件，则用该命令可以对其进行强力删除


$ yum install mariadb-server mariadb 

$ systemctl start mariadb.service  #启动MariaDB
$ systemctl stop mariadb  #停止MariaDB
$ systemctl restart mariadb  #重启MariaDB
$ systemctl enable mariadb  #设置开机启动

$ mysqladmin --version

## 设置新密码
$ mysqladmin -u root password "new_password";

$ mysql -u root -p

## 添加用户访问权限
1. > GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'mypwd' WITH GRANT OPTION;
2. > GRANT ALL PRIVILEGES ON *.* TO 'username'@'%' IDENTIFIED BY 'mypwd' WITH GRANT OPTION;
3. > flush privileges;


## jdbs链接
org.mariadb.jdbc.Driver

jdbc:mariadb://localhost:3306/DB?user=root&password=myPassword


## 更新mariadb-service, 找不到mysql命令
$ yum install -y mariadb-server

## 结束后清理yum
$ yum clean all
