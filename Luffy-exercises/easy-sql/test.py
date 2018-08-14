#!/usr/bin/env python3
#coding:utf-8
#time:2018-08-04

import re
from dml import insertFunc,deleteFunc,updateFunc,findFunc

#增删改查的Pattern
#add staff_table Alex Li,25,134435344,IT,2015-10-29
#${table_name} ${data}
insert_sql = re.compile(r"\s*add\s+(?P<table>\w+)\s+(?P<data>.+)",re.I)

#del from staff where  id=3
#${table_name} ${condition}
#delete_sql = re.compile(r"\s*del\s+from\s+(?P<table>\w+)\s+\
#where\s+(?P<key>\w+)\s*(?P<sign>[>\|<\|=\|like])\s*[\"\']?(?P<value>\w+)[\"\']?",re.I)
delete_sql = re.compile(r"\s*del\s+from\s+(?P<table>\w+)\s+where\s+(?P<key>\w+)\s*(?P<sign>[>\|<\|=\|like])\s*[\"\']?(?P<value>\w+)[\"\']?",re.I)

#UPDATE staff_table SET age=25 WHERE  name ="Alex"
#${table_name} ${condition} ${final_value}
#update_sql = re.compile(r"\s*update\s+(?P<table>\w+)\s+set\s+(?P<ukey>\w+)\s*=\s*[\"\']?(?P<uvalue>\w+)[\"\']?\
#(\s+where\s+(?P<key>\w+)\s*(?P<sign>(>|<|=|like))\s*[\"\']?(?P<value>\w+)[\'\"]?)?",re.I)
update_sql = re.compile(r"\s*update\s+(?P<table>\w+)\s+set\s+(?P<ukey>\w+)\s*=\s*[\"\']?(?P<uvalue>\w+)[\"\']?(\s+where\s+(?P<key>\w+)\s*(?P<sign>(>|<|=|like))\s*[\"\']?(?P<value>\w+)[\'\"]?)?",re.I)

#find * from staff_table where enroll_date like "2013"
#${table_name} ${fields} ${condition}
#find_sql = re.compile(r"\s*find\s+(?P<fields>[\w,*]+)\s+from\s+(?P<table>\w+)(\s+where\s+(?P<key>\w+)\s*(?P<sign>(>|<|=|like))\s*\"?(?P<value>\w+)\"?)?")
#find_sql = re.compile(r"\s*find\s+(?P<fields>[\w,*]+)\s+from\s+(?P<table>\w+)\
#(\s+where\s+(?P<key>\w+)\s*(?P<sign>(>|<|=|like))\s*[\"\']?(?P<value>\w+)[\'\"]?)?",re.I)
find_sql = re.compile(r"\s*find\s+(?P<fields>[\w,*]+)\s+from\s+(?P<table>\w+)(\s+where\s+(?P<key>\w+)\s*(?P<sign>(>|<|=|like))\s*[\"\']?(?P<value>\w+)[\'\"]?)?",re.I)



def start():
    sql = input("请输入您要执行的语句:")

    if insert_sql.match(sql):
        m = insert_sql.match(sql)
        insertFunc(m.groupdict())
    
    elif delete_sql.match(sql):
        m = delete_sql.match(sql)
        deleteFunc(m.groupdict())

    elif update_sql.match(sql):
        m = update_sql.match(sql)
        updateFunc(m.groupdict())
    
    elif find_sql.match(sql):
        m = find_sql.match(sql)
        findFunc(m.groupdict())

    else:
        print ('您输入的语句有语法错误，请检查！')

if __name__ == '__main__':
    start()
    
    