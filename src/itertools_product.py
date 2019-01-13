import itertools


def input_int_list():
    return list(map(int, input().strip().split()))


a = input_int_list()
b = input_int_list()


for p in list(itertools.product(a, b)):
    print(p, end=" ")
