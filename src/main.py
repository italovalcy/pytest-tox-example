import numpy as np

def square(n: float=None) -> float:
    """Square a number."""
    if not n:
        n = np.random.randint(1, 100)
    return n**2
