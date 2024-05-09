sum_of_even_terms = 2
first=1
second=2
while second < 4000000:
    next = first + second
    first = second
    second = next
    if next%2==0:
        sum_of_even_terms += next

print(sum_of_even_terms)