import numpy as np

def matrix_addition(A, B):
    """Performs matrix addition (A + B) using pure Python"""
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrix dimensions must match for addition")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_multiplication(A, B):
    """Performs matrix multiplication using pure Python (nested loops)."""
    if len(A[0]) != len(B):
        raise ValueError("Invalid matrix dimensions for multiplication")
    result = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
    return result

def numpy_matrix_multiplication(A, B):
    """Performs matrix multiplication using NumPy for efficiency."""
    return np.dot(A, B)

    