# 传统Tomcat项目部署问题
在上传项目时, 未添加nginx负载均衡过程中, 需要注意的是, 访问路径为 http://www.name.com:80/app-name/url?param=p

解压tomcat文件夹, 需要修改端口号码, server.xml文件中 将需要修改的port进行修改


