from math import factorial as fac
import time


def func_2(num):
    """
    https://leetcode.com/problems/climbing-stairs/
    """
    cache = {}

    def fact(n):
        if n in cache:
            return cache[n]
        a = 1
        for i in range(n):
            a *= (i + 1)
        cache[n] = a
        return a
    two = num // 2
    one = num % 2
    P = 0
    while one <= num and two >= 0:
        P += fact(one + two)/(fact(one) * fact(two))
        one += 2
        two -= 1
    return int(P)


def func_3(num):
    two = num // 2
    one = num % 2
    P = 0
    while one <= num and two >= 0:
        P += fac(one + two)/(fac(one) * fac(two))
        one += 2
        two -= 1
    return int(P)


if __name__ == "__main__":
    n = 45
    start = time.time()
    print(func_3(n))
    step_1 = time.time()
    print(step_1 - start)
    print(func_2(n))
    print(time.time() - step_1)

