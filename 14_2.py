memory = {}

def collatz_length(n):
    if n in memory:
        return memory[n]
    elif n == 1:
        return 1
    elif n % 2 == 0:
        next_n = n // 2
    else :
        next_n = 3*n+1

    memory[n] = 1 + collatz_length(next_n)  
    return memory[n]

max_length = 1
starting_number_for_max_length = 1    
for i in range(2,1000000):
    length = collatz_length(i)
    if length > max_length:
        max_length = length
        starting_number_for_max_length = i

print("starting number :", starting_number_for_max_length) 
print("length of the chain :", max_length)      