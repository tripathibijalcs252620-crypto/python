print("Squares of numbers from 1 to 10:")
for i in range(1, 11):
    print(i, "square is", i * i)

even_count = 0

print("\nEnter 5 numbers:")
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        even_count += 1

print("\nTotal even numbers entered:", even_count)
