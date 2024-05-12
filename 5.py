number = 20
found = False

while not found:
    found = True
    for i in range(11, 21):
        if number % i:
            found = False
            break

    if found:
        break

    number += 20  # Increment by 20 because the number needs to be divisible by 20

print(number)
