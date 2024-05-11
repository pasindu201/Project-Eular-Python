def isPalindrome(number):
    numberStr = str(number)
    return numberStr == numberStr[::-1]

maxPalindrome = 0
maxI = 0
maxJ = 0

for i in range(100, 999):
    for j in range(100, 999):
        product = i * j
        if isPalindrome(product) and product > maxPalindrome:
            maxPalindrome = product
            maxI = i
            maxJ = j

print("%d x %d = %d" % (maxI, maxJ, maxPalindrome))
