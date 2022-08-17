def reverse_string_recursive(str_val):
    if len(str_val) <= 1:
        return str_val

    return str_val[-1] + reverse_string_recursive(str_val[:-1])


def reverse_string_iterative(str_val):
    value = ""
    for i in range(len(str_val)):
        value = str_val[i] + value
    return value


# print(reverse_string_recursive(""))
# print(reverse_string_recursive("y"))
# print(reverse_string_recursive("yo"))
print(reverse_string_recursive("yoyo mastery"))

# print(reverse_string_iterative(""))
# print(reverse_string_iterative("y"))
# print(reverse_string_iterative("yo"))
print(reverse_string_iterative("yoyo mastery"))

