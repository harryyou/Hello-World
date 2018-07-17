#!/usr/bin/env python3
#coding:utf-8
#D&C 分而治之算法

#use recursvie algorithm to calculate the sum of a list
'''
def sum(l):
    if l:
        return l.pop() + sum(l)
    else:
        return 0
'''
def sum(l):
    if l == []:
        return 0

    return l[0] + sum(l[1:])

#use recursive to calculate the length of a list.
'''
def length(l):
    if l:
        l.pop()
        return 1 + length(l)
    else:
        return 0
'''
def length(l):
    if l == []:
        return 0

    return 1 + length(l[1:])

#use recursive to find the max number of a list.
'''
def largest(l):
    if l:
        max = l.pop()
    for i in l:
        if i > max:
            max = i

    return max
'''
def largest(l):
    if len(l) == 2:
        return l[0] if l[0] > l[1] else l[1]
    sub_max = max(l[1:])
    return l[0] if l[0] > sub_max else sub_max

if __name__ == "__main__":
    l = [i for i in range(101)]
    print(sum(l))
    print(length(l))
    print(largest(l))