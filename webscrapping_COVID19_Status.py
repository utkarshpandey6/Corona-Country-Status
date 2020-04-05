# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 17:04:28 2020

@author: Utkarsh
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re



content = requests.get("https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic_by_country_and_territory#covid19-container")

soup = BeautifulSoup(content.text,"html.parser")

buf  = soup.find('div', attrs={'id':'covid19-container'})
values = buf.text
x = ""
f = 0
for i in range(len(values)):
    
    if(values[i] == '['):
        f=1
    if(values[i] == ']'):
        f=0
    if(f==0 and values[i] != ']' and values[i] !=','):
        x=x+values[i]
        
lis = x.split();
lisnew = []
f=0
for i in lis:
    if(i=="History"):
        break;
    if f==1:
        if (i == "–"):
           lisnew.append("0")
        else:
            lisnew.append(i)
    if(i.isdigit() and f==0):
        lisnew.append("World")
        f=1;
x=""
f=0;
lisnew2 = []
for i in lisnew:
    if (i == "As"):
        f=1
    if i.isdigit() and f==0:
        if len(x)>0:
            lisnew2.append(x)
        lisnew2.append(i)
        x=""
    else:
        if(i=="." or len(x) == 0):
            x=x+i
        else:
            x=x+" "+i
            
            
if len(x) > 0:
    lisnew2.append(x)
    
    
finallis = []

    
for i in range(0,len(lisnew2)-1,4):
    l = []
    l.append(lisnew2[i])
    l.append(lisnew2[i+1])
    l.append(lisnew2[i+2])
    l.append(lisnew2[i+3])
    finallis.append(l)
finallis.append(lisnew2[len(lisnew2)-1])
    

if w=="when":
    print(finallis[len(finallis)-1])
    continue
if w=="all":
    for i in finallis:
        print(i)
    continue;
f=-1
for i in range(len(finallis)-1):
    if(finallis[i][0].lower() == w.lower()):
        f=i
        break;
if f==-1:
    print("No such country found - result 404(not found)")
else:
    print("Country  : ",finallis[f][0])
    print("Cases    : ",finallis[f][1])
    print("Deaths   : ",finallis[f][2])
    print("Recovery : ",finallis[f][3])
    print("result   :"," 202(ok)")
            
    