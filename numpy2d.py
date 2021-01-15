#!/usr/bin/env python3

"""Заполните функции так, чтобы прошли тесты"""


import numpy as np


def sum_all(a):
    """Возвращает сумму всех элементов"""
    pass

def sum_columns(a):
    """Постолбцовая сумма"""
    pass

def sum_rows(a):
    """Построчная сумма"""
    pass

def reorder1(m):
    """На вход подается матрица 2n x 2n, составляет матрицу n x 2n
    из диагональных блоков размером n x n"""
    pass

def reorder2(m):
    """На вход подается матрица 4n x 4n, составляет матрицу 5n x 2n,
    состоящую из вертикально составленных нижнего левого блока 2n x 2n
    и верхнего правого блока 3n x 2n"""
    pass

def main():
    a = np.array([[1, 2, 3,],
                  [4, 5, 6,],
                  [7, 8, 9,]])
    assert sum_all(a) == 45
    assert np.array_equal(sum_columns(a), np.array([12, 15, 18]))
    assert np.array_equal(sum_rows(a), np.array([6, 15, 24]))
    
    m = np.array([[1, 2, 3, 4,],
                  [5, 6, 7, 8,],
                  [9, 10, 11, 12,],
                  [13, 14, 15, 16,]])
    m1 = np.array([[1, 2, 11, 12,],
                   [5, 6, 15, 16,]])
    m2 = np.array([[9, 10],
                   [13, 14],
                   [3, 4],
                   [7, 8],
                   [11, 12]])
    assert np.array_equal(reorder1(m), m1)
    assert np.array_equal(reorder2(m), m2)


if __name__ == '__main__':
    main()
