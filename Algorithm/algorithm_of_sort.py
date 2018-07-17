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


#选择排序
#selection sort
#serarch the index of the smallest one
def findsmallest(l):
    smallest = l[0]
    smallest_index= 0

    for i in range(1,len(l)):
        if l[i] < smallest:
            smallest = l[i]
            smallest_index = i
    return smallest_index

#sort
def selection_sort(l):
    new_l = []

    for i in len(l):
        smallest = findsmallest(l)
        new_l.append(l.pop(smallest))

    return new_l


#冒泡排序
#bubble sort
def bubble_sort(l):
    for i in range(len(l) - 1):          #只需要循环(len(l) - 1)次
        isSorted = True                  #有序标记，每一轮初始默认有序

        for x in range(len(l) - 1 - i):  #每一轮循环，必定会有一个元素添加到有序区域（即末尾的有序区域每次必定至少加1）
            if l[x] > l[x+1]:
                tmp = l[x]
                l[x] = l[x+1]
                l[x+1] = tmp
                isSorted = False         #如果有元素交换，说明不是有序，则继续循环
            
        if isSorted:                     #如果有序，则直接跳出整个循环
            break

    return l


def bubble_sorted(l):
    sortBorder = len(l) - 1

    for i in range(len(l) - 1):
        isSorted = True
        
        for j in range(sortBorder):
            if l[j] > l[j+1]:
                tmp = l[j]
                l[j] = l[j+1]
                l[j+1] = tmp
                isSorted = False  
                lastExchangeIndex = j   #有序数列的边界

        sortBorder = lastExchangeIndex  #下一轮循环只需要边界前面的无序数列进行
        if isSorted:
            break

    return l
