# Program specification
"""
The harmonic sum of an integer, n > 0, can be calculated using the formula .
1 + 1/2 + 1/3 + ... + 1/n
Write a recursive function that computes this.
"""

def harmonic_sum(n):
    """
    A function that returns the harmonic sum of an integer.
    :param n: is an integer > 0
    :return:
    """
    if n == 0:
        return 0
    else:
        return 1 / n + harmonic_sum(n - 1)

print(harmonic_sum(0))
print(harmonic_sum(2))
print(harmonic_sum(4))
print(harmonic_sum(10))
print(harmonic_sum(20))
print(harmonic_sum(100))