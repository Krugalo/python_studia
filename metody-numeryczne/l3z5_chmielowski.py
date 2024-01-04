from scipy.linalg import hilbert
import numpy as np

print("Hilbert(5) =")
print(hilbert(5))
print("Norma =")
print(np.linalg.norm(hilbert(5)))
print("Wskaznik =")
print(np.linalg.cond(hilbert(5)))
print('\n')

print("Hilbert(10) =")
print(hilbert(10))
print("Norma =")
print(np.linalg.norm(hilbert(10)))
print("Wskaznik =")
print(np.linalg.cond(hilbert(10)))
print('\n')

print("Hilbert(20) =")
print(hilbert(20))
print("Norma =")
print(np.linalg.norm(hilbert(20)))
print("Wskaznik =")
print(np.linalg.cond(hilbert(20)))
print('\n')
