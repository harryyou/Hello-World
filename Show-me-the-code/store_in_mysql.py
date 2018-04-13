#!/usr/bin/env python3
#coding:utf-8

import pymysql
from pymysql.err import InternalError, IntegrityError

from generate_active_code import GenerateActiveCode

host = '11.205.50.37'
port = 3306
user = 'club'
passwd = 'club1234'
dbname = 'python'

db = pymysql.connect(host,user,passwd,dbname,port)    #connect to mysql database
cursor = db.cursor()                                  #create cursor

#create table if not exists
create_table = "create table coupon (id int NOT NULL AUTO_INCREMENT ,activate_code char(32) UNIQUE,in_use tinyint default 0,PRIMARY KEY (id))"
try:
    cursor.execute(create_table)                      
except InternalError:
    print ("table is already exists!")


#store data in table coupon
insert_sql = "insert into coupon (activate_code) values ('{0}')"
code = GenerateActiveCode(200)                        #该方法只保证当次生成的激活码不会有重复
for i in code:
    try:
        cursor.execute(insert_sql.format(i))
    except IntegrityError:
        #print (insert_sql.format(i))
        print ("The code" + i + "is already exists!")

cursor.close()
db.commit()
db.close()

