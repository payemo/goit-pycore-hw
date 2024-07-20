from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n : int) -> int:
    """
    Computes the nth Fibonacci number using recursion and memoization.

    Args:
        n (int): The position in the Fibonacci sequence to compute.

    Returns:
        int: The nth Fibonacci number.
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    # print(fibonacci(10))
    # print(fibonacci(15))
    print([fibonacci(n) for n in range(16)])
