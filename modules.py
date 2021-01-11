#!/usr/bin/env python3

"""Напишите модуль mymodule.utils, содержащий функцию swap.
В отличие от других заданий, этот файл исправлять нельзя
"""


from mymodule.utils import swap


def main():
    x = 1
    y = 2
    assert swap(x, y) == (y, x)


if __name__ == '__main__':
    main()
