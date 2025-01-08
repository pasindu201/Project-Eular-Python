# Function to calculate the vertical max product of 4 numbers
def vertical_max_product(matrix, row_start, col_start):
    return (
        matrix[row_start][col_start]
        * matrix[row_start + 1][col_start]
        * matrix[row_start + 2][col_start]
        * matrix[row_start + 3][col_start]
    )

# Function to calculate the horizontal max product of 4 numbers
def horizontal_max_product(matrix, row_start, col_start):
    return (
        matrix[row_start][col_start]
        * matrix[row_start][col_start + 1]
        * matrix[row_start][col_start + 2]
        * matrix[row_start][col_start + 3]
    )

# Function to calculate the diagonal max product of 4 numbers
def diagonal_max_product(matrix, row_start, col_start):
    down_product = (
        matrix[row_start][col_start]
        * matrix[row_start + 1][col_start + 1]
        * matrix[row_start + 2][col_start + 2]
        * matrix[row_start + 3][col_start + 3]
    )
    up_product = (
        matrix[row_start + 3][col_start]
        * matrix[row_start + 2][col_start + 1]
        * matrix[row_start + 1][col_start + 2]
        * matrix[row_start][col_start + 3]
    )
    return down_product, up_product

# Read the matrix from the file
numbers = []
with open("./11/data.txt", 'r') as file:
    number_matrix = []
    lines = file.readlines()
    for line in lines:
        number_matrix.append(list(map(int, line.split())))

# Initialize the result variable
result = 1

# Iterate over the matrix to find the maximum product
for row_number in range(len(number_matrix) - 3):  
    for col_number in range(len(number_matrix[0]) - 3): 
        vertical_product = vertical_max_product(number_matrix, row_number, col_number)
        horizontal_product = horizontal_max_product(number_matrix, row_number, col_number)
        down_product, up_product = diagonal_max_product(number_matrix, row_number, col_number)

        if vertical_product > result:
            result = vertical_product
            numbers = [
                number_matrix[row_number][col_number],
                number_matrix[row_number + 1][col_number],
                number_matrix[row_number + 2][col_number],
                number_matrix[row_number + 3][col_number],
            ]
        if horizontal_product > result:
            result = horizontal_product
            numbers = [
                number_matrix[row_number][col_number],
                number_matrix[row_number][col_number + 1],
                number_matrix[row_number][col_number + 2],
                number_matrix[row_number][col_number + 3],
            ]
        if down_product > result:
            result = down_product
            numbers = [
                number_matrix[row_number][col_number],
                number_matrix[row_number + 1][col_number + 1],
                number_matrix[row_number + 2][col_number + 2],
                number_matrix[row_number + 3][col_number + 3],
            ]
        if up_product > result:
            result = up_product
            numbers = [
                number_matrix[row_number + 3][col_number],
                number_matrix[row_number + 2][col_number + 1],
                number_matrix[row_number + 1][col_number + 2],
                number_matrix[row_number][col_number + 3],
            ]

# Print the result
print(f"The maximum product is: {result}")
print(f"The numbers are: {numbers}")
