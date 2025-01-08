max_length = 1
max_starting_number = 1
for starting_number in range(1, 1000000):
    length = 1
    number = starting_number
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = 3 * number + 1
        length += 1
    if length > max_length:
        max_length = length
        max_starting_number = starting_number

print(max_starting_number)        