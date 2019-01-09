m = int(input())
the_set = set(map(int, input().strip().split()))
n = int(input())

for i in range(n):
    op = input().strip().split()
    if op[0] == "pop":
        the_set.pop()
    elif op[0] == "remove":
        the_set.remove(int(op[1]))
    elif op[0] == "discard":
        the_set.discard(int(op[1]))

print(sum(the_set))
