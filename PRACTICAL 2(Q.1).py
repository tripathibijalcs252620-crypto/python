tup = (10, 20, 30, 40, 50)
print("Original Tuple:", tup)

print("First Element:", tup[0])
print("Last Element:", tup[-1])

print("Middle 3 Elements:", tup[1:4])

tup2 = (60, 70, 80)
result = tup + tup2
print("Concatenated Tuple:", result)

print("Reversed Tuple:", tup[::-1])

tup3 = (1, 2, 3, 2, 4, 2, 5)
count = tup3.count(2)
print("Count of 2:", count)

index = tup3.index(4)
print("Index of 4:", index)

element = 3
if element in tup3:
    print(element, "exists in the tuple")
else:
    print(element, "does not exist in the tuple")

my_list = [100, 200, 300, 400]
tuple_from_list = tuple(my_list)
print("Tuple from List:", tuple_from_list)

num_tuple = (9, 5, 1, 7, 3)
sorted_tuple = tuple(sorted(num_tuple))
print("Sorted Tuple:", sorted_tuple)

repeated_tuple = tup * 3
print("Tuple Repeated 3 Times:", repeated_tuple)

try:
    tup[0] = 99
except TypeError as e:
    print("Tuple is immutable:", e)
