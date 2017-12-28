#!/usr/bin/python
import sys

InputInfo = input ("Please input an integer N (no greater than 1000) and one symbol separated by space")
InputList = InputInfo.split(' ', 1)
N = int(InputList[0])
Symbol = InputList[1]
container = N
if type(N) != type (1) or N <= 0 :
    print("Something goes wrong, you didn't input a positive integer")
    sys.exit()

count = 1
starnum_eachrow = [ 1 ] 
container -= 1
rest_star = 0
while container > 0 :
    count += 1
    need_star_num= 2*count - 1  
    if container >= 2 * need_star_num :
        container -= need_star_num*2
        starnum_eachrow.append(need_star_num)
        starnum_eachrow.insert(0, need_star_num)
    else:
        rest_star = container
        container = 0 
#else:
    # print ("printing index has been generated, %d extra symbols will be discarded ", rest_star)   
row_len = starnum_eachrow[0]
for starnum_thisrow in starnum_eachrow :
    blank_space = int( ( row_len - starnum_thisrow )/2 )
    this_row_print = " " *blank_space + Symbol * int( starnum_thisrow )
    print (this_row_print)

print (rest_star, end = '' )    #To delete the automatic end \n        