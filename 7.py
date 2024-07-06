import math

def isPrime(number):
    if number <=1:
        return False
    for i in range(2,int(math.sqrt(number))+1):
        if(number%i == 0):
            return False    
    return True

count = 0
number = 2

while count <= 10000:
    if isPrime(number):
        count += 1
    number += 1

print("The 10,001th prime number is:", number - 1)
