#!/usr/bin/python3.5
#coding:utf-8
import paramiko
host = '10.133.99.68'
port = '22'
user = 'ebss'
mima = 'picc1234'
paramiko.util.log_to_file('paramiko.log')
server = paramiko.SSHClient()
server.load_system_host_keys()
#不加这段，可能会报'Server not found in known hosts'错误
server.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接主机
server.connect(host, port, user, mima)
#执行命令
stdin, stdout, stderr = server.exec_command('ls -l')
print(stdout.read())
server.close()

