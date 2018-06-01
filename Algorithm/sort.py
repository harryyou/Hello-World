#!/usr/bin/env python3
#coding:utf-8
#sorting algorithm

#quick sort
def quick_sort(l):
    if len(l) < 2:
        return l
    else:
        pivot = l[0]
        smaller = [ i for i in l[1:] if i <= pivot]
        larger = [ i for i in l[1:] if i > pivot]

        return quick_sort(smaller) + [pivot] + quick_sort(larger)



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