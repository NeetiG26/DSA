input_array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def bubble_sort(numbers):
    swaps = 1
    if len(numbers) < 2:
        return numbers
    while swaps:
        for i in range(len(numbers)-1):
            if i == 0:
                swaps = 0
            if numbers[i] > numbers[i+1]:
                swaps = swaps + 1
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

    return numbers


print(bubble_sort(input_array))
# print(bubble_sort([1]))
# print(bubble_sort([0, 2]))
# print(bubble_sort([]))
