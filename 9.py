def find_pythagorean_triple(sum_value):

  for a in range(1, int(sum_value / 3) + 1):  
    for b in range(a, sum_value + 1):  
      c = sum_value - a - b
      if c <= 0: 
        break
      if a**2 + b**2 == c**2:
        return a*b*c

  return None

result = find_pythagorean_triple(1000)

print("Pythagorean Triple :", result)

