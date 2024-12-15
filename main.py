from copy import deepcopy
def find_determinant(mat):
    total_sum = 0
    toggle = 1
    if len(mat) == 1:
        return mat[0][0]
    for i in range(len(mat)):
        matCopy = deepcopy(mat)
        reduce_matrix((matCopy), i, 0)
        total_sum += toggle*mat[0][i]*find_determinant(matCopy)
        toggle *= -1
    return total_sum
def reduce_matrix(mat, x, y):
    #this will remove row y and column x
    mat.pop(y)
    for i in mat:
        i.pop(x)
matrix = []
n = int(input("Matrix Determinant Calculator\nWhat is your matrix length?\n"))
print("input values:")
for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(int(input("Slot at " + str(j + 1) + ", " + str(i + 1))))
for i in matrix:
    print(i)
print("Determinant:", find_determinant(matrix))
