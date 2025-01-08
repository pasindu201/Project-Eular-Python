import time

def count_divisors(num):
    divisors = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors += 2 
    if int(num ** 0.5) ** 2 == num:
        divisors -= 1  
    return divisors

def find_triangle_with_divisors(limit):
    n = 1
    triangle = 1

    while True:
        # Triangle number formula: n * (n + 1) / 2
        triangle = n * (n + 1) // 2

        # Count divisors of n and n+1 separately
        if n % 2 == 0:
            divisors = count_divisors(n // 2) * count_divisors(n + 1)
        else:
            divisors = count_divisors(n) * count_divisors((n + 1) // 2)

        if divisors > limit:
            return triangle

        n += 1

start_time = time.time()
result = find_triangle_with_divisors(500)
end_time = time.time()

print("Time taken:", end_time - start_time)
print("Triangle number with over 500 divisors:", result)
