import numpy as np

def estimate_shaded_area(n):
    """
    Uses Monte Carlo sampling to estimate the area of the shaded region.
    - n: number of random points to generate.
    """
    x = np.random.uniform(0, 2, n)
    y = np.random.uniform(0, 2, n)
    
    m = (((x - 1)**2 + (y - 1)**2 <= 1) & (x ** 2 + y **2 > 4)).sum()
    return 4 * m / n

if __name__ == "__main__":
    sample_sizes = [1_000, 10_000, 100_000, 1_000_000, 10_000_000, 100_000_000]
    for n in sample_sizes:
        est = estimate_shaded_area(n)
        print(f"n = {n:>9}, estimated area ≈ {est:.6f}")
