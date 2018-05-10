#!/usr/bin/env python3
#coding:utf-8
#D&C 分而治之算法

def sum(l):
    if l:
        return l.pop() + sum(l)
    else:
        return 0

if __name__ == "__main__":
    l = [i for i in range(101)]
    print(sum(l))