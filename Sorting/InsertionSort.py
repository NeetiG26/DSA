input_array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def insertion_sort(numbers):
    if len(numbers) < 2:
        return numbers

    p1 = 1
    while p1 < len(numbers):
        if numbers[p1] < numbers[p1-1]:
            for i in reversed(range(1, p1+1)):
                if numbers[i] < numbers[i - 1]:
                    numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
                else:
                    break
        p1 = p1 + 1
    return numbers


print(insertion_sort(input_array))
print(insertion_sort([1]))
print(insertion_sort([0, 2]))
print(insertion_sort([]))
