#!/usr/bin/python  
# -*-coding: UTF-8 -*- 
  
import os  
allFileNum = 0  
def printPath(level, path):  
    global allFileNum  
    ''''' 
    打印一个目录下的所有文件夹和文件 
    '''   
    # 所有文件  
    fileList = []  
    # 返回一个列表，其中包含在目录条目的名称(google翻译)  
    files = os.listdir(path)   
    for f in files:  
        if(os.path.isdir(path + '/' + f)):             
            if(f[0] != '.'):    # 排除隐藏文件夹。因为隐藏文件夹过多  
                print '-' * level, f  
                # 打印目录下的所有文件夹和文件，目录级别+1  
                printPath((level + 1), path + '/' + f)  #recursion 
        if(os.path.isfile(path + '/' + f)):  
            # 添加文件  
            fileList.append(f)  

    for fl in fileList:  
        # 打印文件  
        print '-' * level, fl  
        # 随便计算一下有多少个文件  
        allFileNum = allFileNum + 1  

print "Please enter the directory path you want to list all file info: "		
yourPath = raw_input()
if __name__ == '__main__':  
    printPath(level = 1 , path = yourPath )  
    print '总文件数 =', allFileNum 