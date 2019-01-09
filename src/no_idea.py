def get_input():
    return map(int, input().strip().split())


m, n = tuple(get_input())
the_array = list(get_input())
set_A = set(get_input())
set_B = set(get_input())

happiness = 0

for i in the_array:
    if i in set_A:
        happiness += 1

    if i in set_B:
        happiness -= 1

print(happiness)
