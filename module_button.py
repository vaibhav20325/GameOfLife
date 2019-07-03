# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:15:47 2019

@author: RajeevKumar
"""

def new_button(file_name,x,y):
    list=[]
    f=open(file_name+'.txt','r')
    text=f.readlines()
    l=int(len(text[0].strip()))
    b=int(len(text))
    for i in range(b):
        text[i]=text[i].strip(' ')
    f.close()
    centre_x=l//2
    centre_y=b//2
    
    for i in range(b):
        for j in range(l):
           if text[i][j]=='*':
               list.append((y+i-centre_y,x+j-centre_x))
    return(list)
