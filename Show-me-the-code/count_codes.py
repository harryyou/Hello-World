#!/usr/bin/env python3
#coding:utf-8
#有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

import os
import re

def GetLinesCount(file):
    blank_lines = 0
    comment_lines = 0

    re_blank = re.compile(r"\s*$")
    re_comment = re.compile(r"\s*#")

    with open(file, encoding='utf-8') as f:
        flines = f.readlines()
        total_lines = len(flines)

        for line in flines:
            if re.match(re_blank,line):
                blank_lines += 1
            elif re.match(re_comment,line):
                comment_lines += 1


    return (total_lines,blank_lines,comment_lines)

def CalCodes(path):
    total_counts = [0,0,0,0]
    
    for dir in os.walk(path):
        for i in dir[2]:
            if i.endswith('.py'):
                total_counts[0] += 1

                pyfile = os.path.join(dir[0],i)
                lines = GetLinesCount(pyfile)
                print (pyfile," has {0} total lines, {1} blank_lines, {2} comment_lines!".format(lines[0],lines[1],lines[2]))

                for x in (1,2,3):
                    total_counts[x] += lines[x-1]

    return dict(zip(['total files','total line','blank line','comment line'],list(total_counts)))

if __name__ == '__main__':
    path = "E:\Picc工作文档\harry\Git\Devops-OpenSource\OneStack-master"
    statistics = CalCodes(path)
    print (statistics)







