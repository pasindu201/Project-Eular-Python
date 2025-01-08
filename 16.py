pow = 2**1000
number_str = str(pow)
sum = 0
for x in list(number_str):
    sum += int(x)

print("sum : ", sum)    