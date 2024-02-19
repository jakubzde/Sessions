def divisors(n):
    """
    Returns the divisor of n
    :param n: The number to return the divisors of
    :return: A list of the divisors
    """
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

print(divisors(100))
