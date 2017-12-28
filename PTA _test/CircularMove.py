# This code is designed to adjust given array/list
# by shifting every element by M units rightwards
# circularly
# e.g. a= [1, 2, 3, 4, 5, 6]  M=2 -->
# this input set will give out [5, 6, 1, 2, 3, 4]
# sample input :
# 6 2            (length of array, shift distance)
# 1 2 3 4 5 6    (ellements of array)
############## input processing #################
InputInfo_1 = input("")
InputInfo_2 = input("")
InputList_1 = InputInfo_1.split(' ', 1)
array_len = int( InputList_1[0] ) #get the length of array
shift_dist = int ( InputList_1[1] ) #shift distance rightwards
InputList_2 = InputInfo_2.split(' ', array_len-1 )

originalArray = [0] * array_len #initiate a list with all 0s
for k in range(array_len) :
    originalArray[k] = int( InputList_2[k] ) # Transfer string var to int var

shift_dist = shift_dist % array_len

pre_repository = originalArray[0]  
this_index = ( 0 + shift_dist ) % array_len 
for m in range(array_len) :
    if (shift_dist * (m+1) ) % array_len != 0 :
        post_repository = originalArray[this_index] 
    else:
        post_repository = originalArray[ (this_index +1 ) % array_len]
    originalArray[this_index] = pre_repository
    if (shift_dist * (m+1) ) % array_len != 0 :
        pre_repository = post_repository
        this_index = ( this_index + shift_dist ) % array_len
    else:   
        pre_repository = originalArray[ (this_index +1 ) % array_len]
        this_index = ( this_index + shift_dist + 1 ) % array_len
        
for n in range(array_len - 1):
    print(originalArray[n], end =' ')
print(originalArray[-1])
      

