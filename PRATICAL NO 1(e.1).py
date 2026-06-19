numbers = [12, 45, 7, 23, 89, 34, 56, 10, 67, 5]

print("Original List:", numbers)

maximum = max(numbers)
minimum = min(numbers)
average = sum(numbers) / len(numbers)

print("Maximum Number:", maximum)
print("Minimum Number:", minimum)
print("Average:", average)

ascending = sorted(numbers)
print("Ascending Order:", ascending)

descending = sorted(numbers, reverse=True)
print("Descending Order:", descending)

numbers.append(100)
print("List after adding 100:", numbers)

numbers.pop(0)
print("List after removing the first item:", numbers)
