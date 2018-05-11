#!/usr/bin/env python3
#coding:utf-8
#D&C 分而治之算法

#use recursvie algorithm to calculate the sum of a list.
def sum(l):
    if l:
        return l.pop() + sum(l)
    else:
        return 0

#use recursive to calculate the length of a list.
def length(l):
    if l:
        l.pop()
        return 1 + length(l)
    else:
        return 0

if __name__ == "__main__":
    l = [i for i in range(101)]
    print(sum(l))
    l1 = [ i for i in range(100)]
    print(length(l1))