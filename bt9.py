# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:24:35 2024

@author: HP
"""
a=float(input('nhập a: '))
b=float(input('nhập b: '))

x=((a**(1/2)-b**(1/2))/(a**(1/4)-b**(1/4))) - ((a**(1/2)+(a*b)**(1/4))/(a**(1/4)+b**(1/4)))
print("Ket qua: ",x)
