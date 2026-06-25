numbers = [10, 20, 30, 40, 50, 20, 30, 60, 80]

largest = max(numbers)
print("Largest Number:", largest)

unique_numbers = list(set(numbers))
print("List without Duplicates:", unique_numbers)

even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
print("Number of Even Numbers:", even_count)

user_list = []
for i in range(5):
    n = int(input("Enter a number: "))
    user_list.append(n)
print("Entered List:", user_list)

def average(lst):
    return sum(lst) / len(lst)

print("Average of Entered List:", average(user_list))

text = "Python"
char_list = list(text)
print("List of Characters:", char_list)

words = ['P', 'y', 't', 'h', 'o', 'n']
joined_string = ''.join(words)
print("Joined String:", joined_string)
