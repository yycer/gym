import numpy as np

def gaussian_elimination(A, b):
    """
    Solves a system of linear equations using Gaussian elimination.
    
    Args:
        A: Coefficient matrix
        b: Right-hand side vector
        
    Returns:
        x: Solution vector
    """
    # Create augmented matrix [A|b]
    n = len(b)
    augmented = np.column_stack((A, b)).astype(np.float64)
    
    # Forward elimination
    for i in range(n):
        # Find pivot
        max_row = i + np.argmax(abs(augmented[i:, i]))
        if max_row != i:
            augmented[[i, max_row]] = augmented[[max_row, i]]
            
        pivot = augmented[i, i]
        if abs(pivot) < 1e-10:
            raise ValueError("Matrix is singular or nearly singular")
            
        # Eliminate below
        for j in range(i + 1, n):
            factor = augmented[j, i] / pivot
            augmented[j, i:] -= factor * augmented[i, i:]
    
    # Back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (augmented[i, -1] - np.sum(augmented[i, i+1:n] * x[i+1:])) / augmented[i, i]
        
    return x

if __name__ == "__main__":
    # System of equations from the image:
    # 2x + y - z = 8     (L₁)
    # -3x - y + 2z = -11 (L₂)
    # -2x + y + 2z = -3  (L₃)
    
    A = np.array([
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2]
    ])
    b = np.array([8, -11, -3])
    
    x = gaussian_elimination(A, b)
    print(f"Solution: x = {x}")

