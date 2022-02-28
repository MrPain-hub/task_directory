def func_1(n):
    """
    https://leetcode.com/problems/climbing-stairs/
    """
    def factorial(k1, k2=1):
        """
        k1 > k2
        k1!/(k1-k2)!
        """
        if k1 > k2:
            return k1 * factorial(k1 - 1)
        else:
            return 1


    def Cm_n(m, n):
        """
        n > m
        """
        return factorial(n, m - 1)/factorial(m)



    integer = n//2
    remainder = n % 2

    return factorial(integer)






if __name__ == "__main__":
    n = 3
    print(func_1(n))
