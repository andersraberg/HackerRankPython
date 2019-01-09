if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorted_list = sorted(list(set(arr)), reverse=True)
    print(sorted_list[1])
