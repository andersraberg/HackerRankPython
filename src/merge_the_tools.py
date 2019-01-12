import textwrap


def remove_subsequent(string):
    res = ""
    seen = set([])
    for i in range(len(string)):
        c = string[i]
        if c not in seen:
            res += c
            seen.add(c)

    return res


def merge_the_tools(string, k):
    parts = textwrap.wrap(string, k)
    for i in parts:
        print(remove_subsequent(i))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
