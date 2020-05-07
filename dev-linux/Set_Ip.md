# 设置静态 Ip 地址
```
在简易系统, 安装网络命令
#共享地址: /mnt/hgfs/ $ yum install net-tools -y

虚拟机设置静态IP地址, 修改ip地址
#-1-# 查看当前地址码并复制 centos 7

#-2-# 静态ip修改 $ vi /etc/sysconfig/network-scripts/ifcfg-eth33

TYPE=Ethernet BROWSER_ONLY=no BOOTPROTO=static DEFROUTE=yes IPV4_FAILURE_FATAL=no IPV6INIT=no NAME=ens33 DEVICE=ens33 ONBOOT=yes

gateway 值和虚拟机的值对应
IPADDR=172.16.175.106 GATEWAY=172.16.175.2 NETMASK=255.255.255.0

网管, 我使用的是公司的网管
DNS1=10.2.3.20 DNS2=10.0.3.20

重启网络
$ service network restart

#-3-# 修改主机名称 $ vi /etc/sysconfig/network

HOSTNAME=hadoop100 ## 修改主机名称 NTPSERVERARGS=iburst NETWORKING=yes

#-3.1-# 修改主机名 $ vi /etc/hostname hadoop100

#-4-# 添加主机映射关系配置节点 $ vi /etc/hosts

192.168.174.100 hadoop100 192.168.174.101 hadoop101 192.168.174.102 hadoop102 192.168.174.103 hadoop103 192.168.174.104 hadoop104 192.168.174.105 hadoop105 192.168.174.106 hadoop106 192.168.174.107 hadoop107 192.168.174.108 hadoop108 192.168.174.109 hadoop109

#-4-# 关闭防火墙

重启
$ reboot

检测地址是否正常
$ hostname $ ping www.baidu.com

```