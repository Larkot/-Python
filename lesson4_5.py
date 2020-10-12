from functools import reduce


def some_func(one_elem, selecon_elem):
    return one_elem * selecon_elem

print(f' {reduce(some_func, [el for el in range(99, 1001) if el % 2 == 0])}')