class Matrix:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrices must have the same dimensions for addition.")
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))]
            for i in range(len(self.data))
        ]
        return Matrix(result)

    def __sub__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrices must have the same dimensions for subtraction.")
        result = [
            [self.data[i][j] - other.data[i][j] for j in range(len(self.data[0]))]
            for i in range(len(self.data))
        ]
        return Matrix(result)

    def __mul__(self, other):
        if len(self.data[0]) != len(other.data):
            raise ValueError("Matrices must have compatible dimensions for multiplication.")
        result = [
            [sum(self.data[i][k] * other.data[k][j] for k in range(len(other.data)))
             for j in range(len(other.data[0]))]
            for i in range(len(self.data))
        ]
        return Matrix(result)

    def transpose(self):
        result = [
            [self.data[j][i] for j in range(len(self.data))]
            for i in range(len(self.data[0]))
        ]
        return Matrix(result)

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

# Пример использования
matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)

print("\nAddition:")
print(matrix1 + matrix2)

print("\nSubtraction:")
print(matrix1 - matrix2)

print("\nMultiplication:")
print(matrix1 * matrix2)

print("\nTranspose of Matrix 1:")
print(matrix1.transpose())
