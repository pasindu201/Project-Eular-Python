import math

def isPrime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

count = 0
number = 2

while count < 10000:
    if isPrime(number):
        count += 1
    number += 1

print("The 10,000th prime number is:", number - 1)
