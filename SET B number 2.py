print('2')
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Calculate the sum of columns
column_sums = [sum(col) for col in zip(*matrix)]

# Calculate the sum of rows
row_sums = [sum(row) for row in matrix]

print("Sum of columns:", column_sums)
print("Sum of rows:", row_sums)
