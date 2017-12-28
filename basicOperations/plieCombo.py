def numComb (m,n):
    if n==0:
        return 1
    else:
        if m==0 :
            return numComb(1,n-1)
        else:
            return numComb(m-1,n) + numComb(m+1,n-1)
            
m=0
n= int(raw_input('input a number'))
value=numComb(m,n)
print(value)        