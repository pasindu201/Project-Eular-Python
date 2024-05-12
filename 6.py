sum_of_sqares = 0
square_of_sums = 0
sum = 0

for i in range(1,101):
    sum_of_sqares += i**2
    sum += i

print("sum of sqares : %d", sum_of_sqares)
print("sqare of sums : %d", sum**2)