def fibonacci_recursive(num: int) -> int:
    # O(2^n)
    if num == 0:
        return 0
    if num == 1:
        return 1

    return fibonacci_recursive(num - 1) + fibonacci_recursive(num - 2)


def fibonacci_iterative(num: int) -> int:
    # O(n)
    if num == 0:
        return 0
    if num == 1:
        return 1
    sum_arr = [0, 1]
    for i in range(2, num+1):
        sum_arr.append(sum_arr[-1]+sum_arr[-2])

    return sum_arr[-1]


print(fibonacci_recursive(10))

print(fibonacci_iterative(10))

