import numpy as np

a = np.array([[0, 0, 1, 0, 0],
              [0, 1, 2, 0, 1],
              [2, 0, 0, 0, -1],
              [1, 2, -2, -1, 1],
              [2, -1, 0, 1, -1]])

b = np.array([1, 1, -4, -2, -1])

x = np.linalg.solve(a, b)

print(x)
