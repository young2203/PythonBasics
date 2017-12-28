#!/usr/bin/python
# -*- coding: UTF-8 -*-
 

#fo = open("foo.txt", "wb")
#print "文件名: ", fo.name
#print "是否已关闭 : ", fo.closed
#print "访问模式 : ", fo.mode
#print "末尾是否强制加空格 : ", fo.softspace

#import win32ui
#dlg = win32ui.CreateFileDialog(1) # 1表示打开文件对话框
#dlg.SetOFNInitialDir('C:/') # 设置打开文件对话框中的初始显示目录
#dlg.DoModal()
#filename = dlg.GetPathName() # 获取选择的文件名称

#from Tkinter import *
#from FileDialog import *
#root = Tk()
#fd = LoadFileDialog(root) # 创建打开文件对话框
#filename = fd.go() # 显示打开文件对话框，并获取选择的文件名称
#print filename
#root.mainloop()

# Open keywords list file
import tkFileDialog 
filename = tkFileDialog.askopenfilename(initialdir = 'C:/', title = 'Choose keyword list file') #Obtain directory of object file, including file name

fo = open(filename, "rb")
keywords = fo.read()
print keywords
fo.close()

filedir = tkFileDialog.askdirectory(initialdir = 'E:/', title = 'Choose the directory you want to save new generated xml file')
fw = open(filedir+'/keywords.xml', "w+")
print filedir+'/keywords.xml'
keywords_list = keywords.split(" ")
num = len( keywords_list )

for k in range(num) :
	string_write = '\t'*2+'<KeyWord name="'+keywords_list[k]+'" />\n'
	fw.write(string_write)
	
fw.close()
