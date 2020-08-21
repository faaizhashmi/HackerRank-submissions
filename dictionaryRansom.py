# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 01:18:18 2020

@author: Faaiz Laptop
"""
news="two times three is not four"
msg="two times two is four"
news=news.rstrip().split()
msg=msg.rstrip().split()
notpresent=False
for i in range(0,len(msg)):
    for j in range(0,len(news)):
        if(msg[i]==news[j]) and msg[i]!='':
            msg[i]=''
            news[j]=''
for i in msg:
    if i!='':
        notpresent=True            
if(not notpresent):
    print('Yes')
else:
    print('No')
    





