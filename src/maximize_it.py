import itertools


def sum_of_squares(l):
    return sum(map(lambda x: x * x, l)) % m


k, m = map(int, input().strip().split())

all_lists = list()
for i in range(k):
    all_lists.append(list(map(int, input().strip().split()))[1:])


print(max(list(map(sum_of_squares, itertools.product(*all_lists)))))
