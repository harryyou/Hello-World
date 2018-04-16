#!/usr/bin/env python3
#coding:utf-8

import re

def CountWods(txt):
    word = re.compile(r"\b[A-Za-z]+\b")

    with open(txt) as f:
        l_word = re.findall(word,f.read())

    return l_word


if __name__ == '__main__':
    txt = "123.txt"
    counts = CountWods(txt)
    print (txt + "中单词出现个数为：",len(counts))
    #结果和 ”cat 123.txt|wc -w“的值不一样
