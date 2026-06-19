def swap_elements(lst, index1, index2):
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst

numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

swap_elements(numbers, 1, 3)

print("Updated List:", numbers)
