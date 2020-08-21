# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 02:36:23 2020

@author: Faaiz Laptop
"""

s=['ab','ab','abc']
q=['ab','abc','bc']
dic={}
for i in q:
    count=0
    dic[i]=count
    for j in s:
        if(i==j):
            count+=1
            dic[i]=count
val=[]
for i in dic:
    val.append(dic[i])
print(val)            