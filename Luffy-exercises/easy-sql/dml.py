#!/usr/bin/env python3
#coding:utf-8
#time:2018-08-10
#insert,delete,update,select

import os
import time
import shutil

#数据字典
table = {
    'staff':['id','name','age','phone','job','date'],
    }

#比较函数
#年龄需要转换为int类型，表中还有时间类型，使用dataframe完成此需求比较简单
def makeInt(func):
    def inner(x,y):
        try:
            x = int(x)
            y = int(y)
        except:
            pass
        finally:
            result = func(x,y)
            return result   
    return inner
      
def equal(x,y):
    if x == y: return True
@makeInt
def greater(x,y): 
    if x > y: return True
@makeInt
def smaller(x,y):
    if x < y: return True
def similar(x,y): 
    if x in y: return True

#比较函数字典
compare = {
    '=': equal,
    '>': greater,
    "<": smaller,
    'like': similar,
}



#入参为一个dict，{'table': 'staff_table', 'data': 'Alex Li,25,134435344,IT,2015-10-29'}
def insertFunc(d):
    #先看看表文件是否存在，以及插入的数据长度是否一致
    filename = "{}.txt".format(d['table'])
    if not os.path.exists(filename): raise Exception("当前表不存在!")
    
    length = len(open(filename).readline().split(','))   
    if len(d['data'].split(',')) + 1 == length:
        #last_line = open(filename).readlines()[-1]            #取最后一行，没有判断最后一行是否为空
        last_line = sorted(set(open(filename).readlines()).remove('\n'),key=open(filename).readlines().index)[-1]
        index = int(last_line.split(',')[0]) + 1              #取ID
        data = '\n\n' + str(index) + ',' + d['data']
        with open(filename,'a+') as f:
            f.seek(0)
            for line in f.readlines():
                if line and line != '\n':                     #示例文件里面有空行
                    row = line.split(',')
                    orgniz_data = dict(zip(table[d['table']],row))
                    #print (orgniz_data)
                    if orgniz_data['phone'] == d['data'].split(',')[2].strip():
                        print (line)
                        print ("电话号码重复！")
                        exit(1)
            f.write(data)
        print ("插入完毕，插入数据为：",data)
    
    else:
        print ("插入数据长度不符合要求！")



#入参为一个dict，{'table': 'staff', 'key': 'id', 'sign': '=', 'value': '3'}
def deleteFunc(d):
    #先看看表文件是否存在及系统中有没有该比较符号
    filename = "{}.txt".format(d['table'])
    if not os.path.exists(filename): raise Exception("当前表不存在!")
    assert(d['sign'] in compare)

    delete_count = 0
    #遍历表文件，将不需要删除的行写入到新的表文件中
    with open(filename) as f_old,open(filename+"_new",'w') as f_new:
        for line in f_old.readlines():
            if line and line != '\n':                
                row = line.split(',')
                orgniz_data = dict(zip(table[d['table']],row))
                if compare.get(d['sign'])(orgniz_data[d['key']],d['value']):   #这个地方不用get，当sql中没有对应字段时报错
                    print ("删除此条数据",line)
                    delete_count += 1
                    continue
           
            f_new.write(line)
    shutil.move(filename,filename + time.strftime("%Y%m%d-%H%M%S",time.localtime()))
    shutil.move(filename+"_new", filename)
    print ("本次操作一共删除了{}条数据!".format(delete_count))
    
    
#入参为一个dict，{'table': 'staff_table','ukey': 'age','uvalue': '25','key': 'name','sign': '=','value': 'Alex'}
def updateFunc(d):
    filename = "{}.txt".format(d['table'])
    if not os.path.exists(filename): raise Exception("当前表不存在！")
    assert(d['sign'] in compare)

    update_count = 0
    #遍历表文件，将匹配到的行修改后写入新文件
    with open(filename) as f_old, open(filename+"_new",'w') as f_new:
        for line in f_old.readlines():
            if line and line !='\n':
                row = line.split(',')
                orgniz_data = dict(zip(table[d['table']],row))
                if compare.get(d['sign'])(d['value'],orgniz_data[d['key']]):   #这个地方不用get，当sql中没有对应字段时报错
                    print ("更新前的数据：",line)
                    orgniz_data[d['ukey']] = d['uvalue']
                    line = ','.join(list(orgniz_data.values()))
                    print ("更新后的数据：",line)
                    update_count += 1
            
            f_new.write(line)
    shutil.move(filename,filename + time.strftime("%Y%m%d-%H%M%S",time.localtime()))
    shutil.move(filename+"_new",filename)
    print ("本次操作一共更新了{}条数据！".format(update_count))
            

#{'fields': '*','table': 'staff_table','key': 'enroll_date','sign': 'like','value': '2013'}
#假设所有sql都加了where
def findFunc(d):
    filename = "{}.txt".format(d['table'])
    if not os.path.exists(filename): raise Exception("当前表不存在！")

    select_count = 0
    with open(filename) as f:
        for line in f.readlines():
            if line and line != '\n':
                row = line.split(',')
                orgniz_data = dict(zip(table[d['table']],row))
                if compare.get(d['sign'])(orgniz_data[d['key']],d['value']):
                    if d['fields'] == "*":
                        print (row) 
                    else:
                        fields = d['fields'].split(',')
                        row = []
                        for i in fields:
                            row.append(orgniz_data[i.strip()])
                        print (row)
                    
                    select_count += 1
    print ("一共查询出了{}条数据！".format(select_count))
                    

