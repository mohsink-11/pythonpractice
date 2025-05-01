import math
def is_Prime(n):
    primeNumbers=[]
    
    for i in range(2,n+1):
        isPrime=True
        for j in range(2,int(math.sqrt(i))+1):
            if i%j == 0:
                isPrime=False
                break
        if(isPrime):
            primeNumbers.append(i)
    return primeNumbers

print(is_Prime(19)) # True

