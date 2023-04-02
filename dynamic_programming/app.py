def dynamic_fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    if lookup[n] is not None:
        return lookup[n]

    lookup[n] = dynamic_fibonacci(n - 1) + dynamic_fibonacci(n - 2)
    return lookup[n]


lookup = [None] * 1000  # store 1000 items in the lookup list


for i in range(20):
    print(dynamic_fibonacci(i))
