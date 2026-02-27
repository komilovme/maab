import numpy as np

# 1. Vector 10 → 49
v1 = np.arange(10, 50)
print("1. Vector 10-49:\n", v1)

# 2. 3x3 matrix 0 → 8
m2 = np.arange(9).reshape(3, 3)
print("\n2. 3x3 Matrix 0-8:\n", m2)

# 3. 3x3 Identity matrix
identity = np.eye(3)
print("\n3. Identity Matrix:\n", identity)

# 4. 3x3x3 random array
arr3d = np.random.random((3, 3, 3))
print("\n4. 3x3x3 Random Array:\n", arr3d)

# 5. 10x10 random + min/max
m5 = np.random.random((10, 10))
print("\n5. Min:", m5.min(), "Max:", m5.max())

# 6. Random vector size 30 + mean
v6 = np.random.random(30)
print("\n6. Mean:", v6.mean())

# 7. Normalize 5x5 random matrix
m7 = np.random.random((5, 5))
m7_norm = (m7 - m7.min()) / (m7.max() - m7.min())
print("\n7. Normalized Matrix:\n", m7_norm)

# 8. Matrix multiplication 5x3 * 3x2
A8 = np.random.random((5, 3))
B8 = np.random.random((3, 2))
product8 = np.dot(A8, B8)
print("\n8. Matrix Product (5x3 * 3x2):\n", product8)

# 9. Dot product of two 3x3 matrices
A9 = np.random.random((3, 3))
B9 = np.random.random((3, 3))
dot9 = np.dot(A9, B9)
print("\n9. Dot Product 3x3:\n", dot9)

# 10. Transpose of 4x4 matrix
m10 = np.random.random((4, 4))
print("\n10. Transpose:\n", m10.T)

# 11. Determinant of 3x3 matrix
m11 = np.random.random((3, 3))
det11 = np.linalg.det(m11)
print("\n11. Determinant:", det11)

# 12. Matrix product A(3x4) * B(4x3)
A12 = np.random.random((3, 4))
B12 = np.random.random((4, 3))
product12 = np.dot(A12, B12)
print("\n12. A(3x4) * B(4x3):\n", product12)

# 13. Matrix-vector product
A13 = np.random.random((3, 3))
v13 = np.random.random((3, 1))
result13 = np.dot(A13, v13)
print("\n13. Matrix-Vector Product:\n", result13)

# 14. Solve Ax = b
A14 = np.array([[3, 1, 2],
                [1, 4, 0],
                [2, 0, 5]])
b14 = np.array([10, 12, 13])
x14 = np.linalg.solve(A14, b14)
print("\n14. Solution x:\n", x14)

# 15. Row-wise and Column-wise sums (5x5)
m15 = np.random.random((5, 5))
row_sum = m15.sum(axis=1)
col_sum = m15.sum(axis=0)
print("\n15. Row sums:\n", row_sum)
print("Column sums:\n", col_sum)