#!/usr/bin/python  
# -*-coding: UTF-8 -*- 
  
import os  
allFileNum = 0  
def printPath(level, path):  
    global allFileNum  
    ''''' 
    ��ӡһ��Ŀ¼�µ������ļ��к��ļ� 
    '''   
    # �����ļ�  
    fileList = []  
    # ����һ���б����а�����Ŀ¼��Ŀ������(google����)  
    files = os.listdir(path)   
    for f in files:  
        if(os.path.isdir(path + '/' + f)):             
            if(f[0] != '.'):    # �ų������ļ��С���Ϊ�����ļ��й���  
                print '-' * level, f  
                # ��ӡĿ¼�µ������ļ��к��ļ���Ŀ¼����+1  
                printPath((level + 1), path + '/' + f)  #recursion 
        if(os.path.isfile(path + '/' + f)):  
            # ����ļ�  
            fileList.append(f)  

    for fl in fileList:  
        # ��ӡ�ļ�  
        print '-' * level, fl  
        # ������һ���ж��ٸ��ļ�  
        allFileNum = allFileNum + 1  

print "Please enter the directory path you want to list all file info: "		
yourPath = raw_input()
if __name__ == '__main__':  
    printPath(level = 1 , path = yourPath )  
    print '���ļ��� =', allFileNum 