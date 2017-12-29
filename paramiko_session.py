#/bin/usr/env python2.7
#coding:utf-8

import paramiko

#设置ssh连接的远程主机地址和端口
host = paramiko.Transport((ip, port))

#设置登录名和密码
host.connect(username=username,password=password)

#连接成功后打开一个channel
session = host.open_session()

#设置会话超时时间
host.settimeout(time)

#打开远程的terminal
host.get_pty()

#激活terminal
host.invoke_shell()

#远程执行命令
host.send('command')

#获取本地反馈
feedback = host.recv(recv_buffer)

#设置延时
time.sleep(time)

#使用条件循环
while not feedback.endswith('#')
	feedback=host.recv(recv_buffer)
