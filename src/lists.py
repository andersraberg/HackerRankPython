if __name__ == '__main__':
    N = int(input())
    the_list = []
    for i in range(N):
        op = input().strip().split(" ")
        if op[0] == "insert":
            the_list.insert(int(op[1]), int(op[2]))
        elif op[0] == "print":
            print(the_list)
        elif op[0] == "remove":
            the_list.remove(int(op[1]))
        elif op[0] == "append":
            the_list.append(int(op[1]))
        elif op[0] == "sort":
            the_list.sort()
        elif op[0] == "pop":
            the_list.pop()
        elif op[0] == "reverse":
            the_list.reverse()
