digits = ""
try:
  with open("./8/number.txt", 'r') as file_object:
    numbers_str = file_object.read()
    digits = numbers_str.replace("\n", "")
except FileNotFoundError:
  print("Error: File 'names.txt' not found.")

except Exception as e:  
  print(f"An error occurred: {e}")

max_product = 0  

for i in range(len(digits) - 12):  
    product = 1
    for j in range(13):
        product *= int(digits[i + j]) 
    max_product = max(max_product, product)

print(max_product)