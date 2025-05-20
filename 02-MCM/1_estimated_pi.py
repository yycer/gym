import numpy as np

def estimate_pi(n):
    """
    Uses Monte Carlo sampling to estimate the value of π.
    - n: number of random points to generate.
    """
    # Generate n random (x, y) pairs in [-1, 1] × [-1, 1]
    x = np.random.uniform(-1, 1, n)
    y = np.random.uniform(-1, 1, n)
    
    # Count how many fall inside the unit circle x^2 + y^2 <= 1
    inside_circle = (x**2 + y**2) <= 1
    m = inside_circle.sum()
    
    # Estimate π as the fraction inside times area factor 4
    pi_est = 4 * m / n
    return pi_est

# Example usage
if __name__ == "__main__":
    sample_sizes = [1_000, 10_000, 100_000, 1_000_000, 10_000_000, 100_000_000]
    for n in sample_sizes:
        est = estimate_pi(n)
        print(f"n = {n:>9}, estimated π ≈ {est:.6f}")
