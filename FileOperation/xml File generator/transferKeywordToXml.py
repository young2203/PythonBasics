#!/usr/bin/python
# -*- coding: UTF-8 -*-
 

#fo = open("foo.txt", "wb")
#print "�ļ���: ", fo.name
#print "�Ƿ��ѹر� : ", fo.closed
#print "����ģʽ : ", fo.mode
#print "ĩβ�Ƿ�ǿ�Ƽӿո� : ", fo.softspace

#import win32ui
#dlg = win32ui.CreateFileDialog(1) # 1��ʾ���ļ��Ի���
#dlg.SetOFNInitialDir('C:/') # ���ô��ļ��Ի����еĳ�ʼ��ʾĿ¼
#dlg.DoModal()
#filename = dlg.GetPathName() # ��ȡѡ����ļ�����

#from Tkinter import *
#from FileDialog import *
#root = Tk()
#fd = LoadFileDialog(root) # �������ļ��Ի���
#filename = fd.go() # ��ʾ���ļ��Ի��򣬲���ȡѡ����ļ�����
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
