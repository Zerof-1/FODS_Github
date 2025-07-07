import numpy as np

def input_matrix(name):
    rows = int(input(f"Enter number of rows for Matrix {name}: "))
    cols = int(input(f"Enter number of columns for Matrix {name}: "))
    print(f"Enter values for Matrix {name} (row by row):")
    matrix = []

    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != cols:
            raise ValueError(f"Each row must have exactly {cols} values.")
        matrix.append(row)

    return np.array(matrix)

try:
    # Input two matrices
    A = input_matrix("A")
    B = input_matrix("B")

    print("\nMatrix A:\n", A)
    print("Matrix B:\n", B)

    # Addition and Subtraction: same shape required
    if A.shape == B.shape:
        print("\nAddition:\n", A + B)
        print("\nSubtraction:\n", A - B)
    else:
        raise ValueError("Addition/Subtraction requires matrices of the same dimensions.")

    # Multiplication: A.cols must match B.rows
    if A.shape[1] == B.shape[0]:
        print("\nMultiplication:\n", np.dot(A, B))
    else:
        raise ValueError("Matrix multiplication requires A.columns == B.rows")

except ValueError as ve:
    print("Error:", ve)
except Exception as e:
    print("Unexpected error:", e)
