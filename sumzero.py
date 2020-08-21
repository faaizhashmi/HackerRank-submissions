#str1="<div><b><p>hello world</p></b></div>"
#str2=[]
#str3=[]
#for i in range(0,len(str1)):
#    if str1[i] =='<'and str1[i+1]!='/':
#        str2.append(str1[i+1])
#    if str1[i]=='<' and str1[i+1]=='/':
#        str3.append(str1[i+2])
#print(str2)
#print(str3) 
#str4=str3[::-1]
#print(str4)
#while(1):
#    if(len(str4)<=0 or len(str2)<=0):
#        break
#    else:
#        if(str4.pop()==str2.pop()):
#            print("Yes")

 
from itertools import groupby
strArr=["R","(x,x,x,x,x,x,x)","(x,x,x,x,x,x,x)","(x,x,x,x,x,x,x)","(x,x,x,R,x,x,x)","(x,x,x,R,x,x,x)","(x,x,x,R,Y,Y,Y)"]
strArr=[1, 2, 3, 4, 5, 5, 6]
#board=strArr[1:]
print(any(sum(1 for _ in g) >3 for _, g in groupby(strArr)))