#!/usr/bin/env python3
#coding:utf-8

import string
import random

def GenerateActiveCode(n):
    
    ''' 多次调用该方法，还是有可能会生成重复的激活码 '''

    code_set = set()
    while len(code_set) < n:
        code = ''.join(random.sample(string.ascii_uppercase+string.digits,16))
        code_set.add(code)
    
    return code_set
    
if __name__ == "__main__":
print(GenerateActiveCode(200))