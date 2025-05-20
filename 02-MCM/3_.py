import numpy as np

def f(x):
    """
    The function f(x) = 1 / (1 + (sin x) * (ln x)^2)
    """
    return 1 / (1 + np.sin(x) * (np.log(x))**2)

def estimate_integral_monte_carlo(a, b, n):
    """
    Uses Monte Carlo sampling to estimate the integral of f(x) from a to b.
    - a, b: integration limits
    - n: number of random points to generate
    """
    # Generate n random x values in [a, b]
    x = np.random.uniform(a, b, n)
    
    # Evaluate the function at these points
    y = f(x)
    
    # Estimate the integral as the average value of f(x) times the interval width
    integral_est = (b - a) * np.mean(y)
    
    return integral_est

if __name__ == "__main__":
    # Integration limits
    a = 0.8
    b = 3
    
    # Sample sizes to try
    sample_sizes = [1_000, 10_000, 100_000, 1_000_000, 10_000_000]
    
    print(f"Estimating the integral of f(x) = 1/(1 + (sin x)*(ln x)^2) from {a} to {b}")
    print("-" * 60)
    
    for n in sample_sizes:
        est = estimate_integral_monte_carlo(a, b, n)
        print(f"n = {n:>9}, estimated integral ≈ {est:.6f}")
