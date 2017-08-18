# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 21:32:40 2017

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 11:01:40 2017

@author: Administrator
"""

import requests
from bs4 import BeautifulSoup
def luqu(a,b,x,c):
    url = "http://www.sneac.com/gklqcx/gklqdtcx_jg.jsp?wbtreeid=3076"
    head = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
    playload = {
        "wbzkzh":a,
        "wbsfzh":b
        }
    req = requests.post(url,headers = head,data = playload)
    soup = BeautifulSoup(req.text,'html.parser')
    aaa = soup.select('.shstyle679706692_3159')
    if aaa:
        pass
    else:
        print(x+","+c)


f = open(r"e:\xin.txt",'rb')
for i in f:
    try:
        xx = i.decode("gbk")
    except UnicodeDecodeError:
       pass
    j = xx.split(",")
    
    x = j[0]
    a = j[1]
    b = j[2]
    c = j[3]
    
    luqu(a,b,x,c)
f.close()
