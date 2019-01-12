def print_formatted(number):
    for i in range(number):
        w = len("{:b}".format(number))
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".
              format(i + 1, width=w))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
