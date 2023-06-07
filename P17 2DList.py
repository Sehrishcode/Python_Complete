twoD_matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(twoD_matrix[0])
print(twoD_matrix[1])
print(twoD_matrix[0][1])
twoD_matrix[0][1] = 20
print(twoD_matrix[0][1])
for row in twoD_matrix:
    for item in row:
        print(item)
