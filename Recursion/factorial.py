def factorial_recursion(num: int) -> int:
    if num <= 1:
        return 1

    return num*factorial_recursion(num-1)


def factorial_iterative(num: int) -> int:

    if num <= 1:
        return 1
    fact = 1
    for i in range(1, num+1):
        fact = i*fact

    return fact


print(factorial_recursion(5))

print(factorial_iterative(5))

