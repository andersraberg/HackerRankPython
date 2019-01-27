n = int(input())
for i in range(n):
    try:
        a, b = input().strip().split()
        print(int(a) / int(b))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code: {}".format(e))
