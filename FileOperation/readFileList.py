#!/usr/bin/python  
# -*-coding: UTF-8 -*- 
  
import os  
allFileNum = 0  
def printPath(level, path):  
    global allFileNum  
    ''''' 
    ��ӡһ��Ŀ¼�µ������ļ��к��ļ� 
    '''  
    # �����ļ��У���һ���ֶ��Ǵ�Ŀ¼�ļ���  
    dirList = []  
    # �����ļ�  
    fileList = []  
    # ����һ���б����а�����Ŀ¼��Ŀ������(google����)  
    files = os.listdir(path)  
    # �����Ŀ¼����  
    dirList.append(str(level))  
    for f in files:  
        if(os.path.isdir(path + '/' + f)):  
            # �ų������ļ��С���Ϊ�����ļ��й���  
            if(f[0] == '.'):  
                pass  
            else:  
                # ��ӷ������ļ���  
                dirList.append(f)  
        if(os.path.isfile(path + '/' + f)):  
            # ����ļ�  
            fileList.append(f)  
    # ��һ����־ʹ�ã��ļ����б��һ�����𲻴�ӡ  
    i_dl = 0  
    for dl in dirList:  
        if(i_dl == 0):  
            i_dl = i_dl + 1  
        else:  
            # ��ӡ������̨�����ǵ�һ����Ŀ¼  
            print '-' * (int(dirList[0])), dl  
            # ��ӡĿ¼�µ������ļ��к��ļ���Ŀ¼����+1  
            printPath((int(dirList[0]) + 1), path + '/' + dl)  #recursion
    for fl in fileList:  
        # ��ӡ�ļ�  
        print '-' * (int(dirList[0])), fl  
        # ������һ���ж��ٸ��ļ�  
        allFileNum = allFileNum + 1  

print "Please enter the directory path you want to list all file info: "		
yourPath = raw_input()
if __name__ == '__main__':  
    printPath(level = 1 , path = yourPath )  
    print '���ļ��� =', allFileNum 