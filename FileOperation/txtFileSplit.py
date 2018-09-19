import os
filename = 'pg5200_thisone.txt'
file_num = 8
byte_count = 0  # Count for the size of file
full_text = [] #Initialize empty lsit for string storage
with open(filename) as f:
    for line in f:
        full_text.append(line)
        byte_count += len(line)
subCount = byte_count / file_num # Get size of chunk file after splitting

line_num = 0
size_check = 0
size_check += len(full_text[0])
for i in range(file_num-1):
    fname = filename+'_{0:02d}.txt'.format(i)
    f = open(fname, 'w')
    while (size_check <= subCount*(i+1)): 
        f.write(full_text[line_num])
        line_num +=1
        size_check += len(full_text[line_num])
    f.close()
    

fname = filename+'_{0:02d}.txt'.format(file_num-1)
f = open(fname, 'w')
for i in range(line_num, len(full_text),1):   
    f.write(full_text[i])
f.close()    


for i in range(file_num):
    print(os.path.getsize(filename+'_{0:02d}.txt'.format(i)))
#     print(os.path.getsize('pg5200_thisone.txt_01.txt'))
#     print(os.path.getsize('pg5200_thisone.txt_02.txt'))