#!/usr/bin/env python3
#coding:utf-8

from generate_active_code import GenerateActiveCode
from rediscluster import StrictRedisCluster
from redis.exceptions import ResponseError
from datetime import datetime

startup_nodes = [{"host": "10.10.68.242", "port": "8011"},{"host": "10.10.68.242", "port": "8012"},{"host": "10.10.68.242", "port": "8013"},{"host": "10.10.68.242", "port": "9011"},{"host": "10.10.68.242", "port": "9012"},{"host": "10.10.68.242", "port": "9013"}]
#startup_nodes = [{"host": "10.10.68.242", "port": "8011"}]
passwd = 'redis1234'

#key name
time = datetime.now().strftime('%Y%m%d')
key_name = "activate_code_" + time
print ("key name is:",key_name)

#generate activate code
tcode = GenerateActiveCode(200)

#get redis cluster connection
rc = StrictRedisCluster(startup_nodes=startup_nodes,decode_responses=True,password=passwd)

#to store code in redis list
#map(lambda v:rc.lpush(keyname,v),[i for i in tcode])
for i in tcode:
    try:
        rc.lpush(key_name,i)
        print (i)
    except ResponseError as e:
        print ("failed to store code:",i)
        print (e)

print ("total numbes:",rc.llen(key_name))

'''
不知道为什么，多次调用脚本，有时会如下错误：
redis.exceptions.ConnectionError: Error 10060 connecting to .
由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。

strictRedis() 没有实现关闭连接的方法
'''


