"""
Приведены 2 алгоритма определения числа Фибоначчи
    - (Функция) без рекурсии, перестановкой за O(n)
    - (Класс) матричный способ с использованием numpy за O(log n)
"""
import numpy as np
import time


def fid_dynamic(n):
    """
    Без рекурсии
    за время O(n)
    """
    n_1 = 0
    n_2 = 1
    for _i in range(n):
        n_1, n_2 = n_2, n_1 + n_2
    return n_1


class FiboMatrix:
    """
    Матричный способ определения
    с использованием numpy
    за время O(log n)
    """
    def __init__(self):
        self.Q = np.array([[1, 1], [1, 0]])
        self.__cache = {}

    def __get_matrix_power(self, M, p):
        """
        Возведение матрицы в степень
        """

        if p == 1:
            return M
        if p in self.__cache:
            return self.__cache[p]
        K = self.__get_matrix_power(M, int(p/2))
        R = np.dot(K, K)
        self.__cache[p] = R
        return R

    def get_number(self, n):
        """
        Получение n-го числа Фибоначчи
        """
        if n < 2:
            return n
        """
        Разложение степени на степени, равные степени двойки,
        62 = 2^5 + 2^4 + 2^3 + 2^2 + 2^0 = 32 + 16 + 8 + 4 + 1
        """
        powers = [int(pow(2, b))
                  for (b, d) in enumerate(reversed(bin(n-1)[2:])) if d == '1']

        matrices = [self.__get_matrix_power(self.Q, p)
                    for p in powers]
        while len(matrices) > 1:
            M1 = matrices.pop()
            M2 = matrices.pop()
            R = np.dot(M1, M2)
            matrices.append(R)
        return matrices[0][0][0]


if __name__ == "__main__":
    start = time.time()
    N = 300

    mfib = FiboMatrix()
    for n in range(0, N):
        print(mfib.get_number(n), end=' ')
    time_1 = time.time() - start
    print()

    for n in range(0, N):
        num = mfib.get_number(n)
        print(fid_dynamic(n), end=' ')
    time_2 = time.time() - (time_1 + start)
    print()
    print(f"mfib за время {time_1}")
    print(f"fid_dynamic за время {time_2}")
