# -*- coding: utf-8 -*-
import sys
#sys.path.append('C:\Users\young\Python\Python_testspace')
#of = open('C:\Users\young\Python\Python_testspace\ref_list.tex')
fo = open('C:\Users\young\Python\Python_testspace\ref_list.txt') #read file with binary form
lines = fo.readlines()
for line in lines:
    print(line)
of.close()

