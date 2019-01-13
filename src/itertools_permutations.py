import itertools


the_str, size = input().strip().split()


for p in sorted(list(map("".join,
                         list(itertools.permutations(the_str, int(size)))))):
    print(p)
