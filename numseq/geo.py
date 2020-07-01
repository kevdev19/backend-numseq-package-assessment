def square(n):
    """Returns the nth term of numbers that can be arranged
    into square geometric shape [1, 4, 9, 16, 25] """

    result = [num * num for num in range(n)]

    return result[1:]


def triangle(n):
    """Returns the nth term of numbers that can be arranged in
    triangular geometric shapes [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    """
    j = 1
    k = 1
    result = []
    for num in range(1, n + 1):
        result.append(num)
        j = j + 1
        k = k + j

    return result


def cube(n):
    """
    Returns the nth term of the numbers that can be arranged
    as symmetric cube shapes [1, 8, 27, 64]
    """
    result = [num*num*num for num in range(n)]

    return result[1:]
