# Reverse a list
n = int(input("Enter number to generate a range of numbers from 0 to end point: "))
numbers = list(range(0, n+1))
print("Generated List:")
print(numbers)
print("Reverse List:")
print(numbers[::-1])