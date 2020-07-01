def fib(n):
    """
    Returns the nth Fibonacci number
    The first 10 terms are: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()
