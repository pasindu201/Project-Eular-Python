import math

def isprime(number):
    for i in range(2,int(math.sqrt(number))+1):
       if number%i == 0:
        return False
    return True

sum = 0    

for j in range(3, 2000000):
   if isprime(j):
     sum += j

print("sum of primes : ", sum)     