# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 09:01:33 2020

@author: Arzoo
"""


t=int(input())
for z in range(t):
    size=int(input())
    l=[]
    for j in range(size):
       s=input()
       ln=s.split(" ")
       l.append(ln)
    dia=0
    for i in range(len(l)):
        dia=dia+int(l[i][i])
    r=0
    for i in range(size):
        count=0
        for j in range(size):
            temp=l[i][j]
            for k in range(j+1,size):
                if(l[i][k]==temp):
                    count+=1
                    r+=1
                    break
            if(count==1):
                break
    c=0
    for i in range(size):
        count=0
        for j in range(size):
            temp=l[j][i]
            for k in range(j+1,size):
                if(l[k][i]==temp):
                    count+=1
                    c+=1
                    break
            if(count==1):
                break
    print("Case #{}: {} {} {}".format(z,dia,r,c))
    
    