'''
Created on Mar 11, 2017
# This code is used to solve prime number pair guess problem
# It will ask you to input a integer no greater than 10^5
# then it will output the number of prime pairs which satisfy
# the difference between these two primes exactly equal 2
# e.g. (3,5) is a prime pair, 5 -3 = 2, thus this is a qualified
# prime pair, (11, 7) is another pair, while 11 -7 = 4 , so this
# is not the pair we are looking for 
@author: young
'''
from math import sqrt

def getPrimeList ( N = 1000 ):
    primeList = [2]
    for num in range(3, N+1, 2) :
        if isPrime ( num ) :
            primeList.append(num)
    return primeList

def isPrime ( num_input ):
    factor = 2
    while  factor <= sqrt (num_input) :
        if num_input % factor == 0:
            return False
            break
        else :
            factor += 1
    else :
        return True

N = input("")  # get the input Integer        
myPrimeList = getPrimeList ( int(N) ) #get the list of prime less than N  
  
counter = 0
for sub_no in range( len(myPrimeList) - 1) :
    if myPrimeList[sub_no] + 2 == myPrimeList[sub_no+1] :
        counter +=1

print (counter)   