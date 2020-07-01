def primes(n):
    """
    Returns a list of all prime number less than n
    """
    for num in range(1, n):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
                else:
                    return num


def is_prime(n):
    """
    Returns a boolean indicating whether m is a prime number
    """

    for num in range(1, n):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                return True
