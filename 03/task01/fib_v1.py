from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    """
    Returns a Fibonacci function with memoization to optimize repeated calculations.

    Returns:
        Callable[[int], int]: A function that computes the nth Fibonacci number.
    """
    cache = dict()

    def fibonacci(n : int) -> int:
        """
        Computes the nth Fibonacci number using recursion and memoization.

        Args:
            n (int): The position in the Fibonacci sequence to compute.

        Returns:
            int: The nth Fibonacci number.
        """
        nonlocal cache

        if n <= 0:
            return 0
        if n == 1: 
            return 1
        if n in cache:
            return cache[n]

        # Calculate and cache the nth Fibonacci number
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci

if __name__ == '__main__':
    fib = caching_fibonacci()

    # print(fib(10))
    # print(fib(15))

    print([fib(n) for n in range(16)])