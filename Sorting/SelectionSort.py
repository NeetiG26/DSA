input_array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def selection_sort(numbers):
    if len(numbers) < 2:
        return numbers

    updated_index = 0
    while updated_index < len(numbers):
        new_list = numbers[updated_index:]
        min_index = numbers.index(min(new_list))
        numbers[updated_index], numbers[min_index] = numbers[min_index], numbers[updated_index]
        updated_index = updated_index + 1

    return numbers


print(selection_sort(input_array))
print(selection_sort([1]))
print(selection_sort([0, 2]))
print(selection_sort([]))
