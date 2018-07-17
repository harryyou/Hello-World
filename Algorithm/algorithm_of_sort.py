#!/usr/bin/env python3
#coding:utf-8
#sorting algorithm

#快速排序
#quick sort
def quick_sort(l):
    if len(l) < 2:
        return l
    else:
        pivot = l[0]
        smaller = [ i for i in l[1:] if i <= pivot]
        larger = [ i for i in l[1:] if i > pivot]

        return quick_sort(smaller) + [pivot] + quick_sort(larger)