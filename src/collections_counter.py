def input_int_list():
    return list(map(int, input().strip().split()))


number_of_shoes = int(input())
shoe_sizes = input_int_list()
number_of_customers = int(input())

customers = []
for i in range(number_of_customers):
    size, price = input_int_list()
    customers.append((size, price))

money_sum = 0
for c in customers:
    if c[0] in shoe_sizes:
        money_sum += c[1]
        shoe_sizes.remove(c[0])

print(money_sum)
