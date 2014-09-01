__author__ = 'Tyraan'
from functools import reduce
from fractions import gcd
def getPrime(number):
    result = []
    # 先將質數2去除

    while number % 2 == 0:
        number = number / 2
        result.append(2)
    current = 3
    while number != 1:
        while number % current == 0:
                number  = number / current
                result.append(current)
        current = current + 2
    return result

def gcm(a,b):
    return (a*b)/gcd(a,b)


def lcm(*args):
    return reduce(lambda x,y: x * y / gcd(x,y), args)
