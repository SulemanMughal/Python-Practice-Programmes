# Swap two numbers without third variable

# First Number
n = int(input("Enter first number:\t"));

# Second Number
n1 = int(input("Enter second number:\t"));

print("Numbers before swapping : ")
print("First number : ", n)
print("Second Number : ", n1)

n, n1 = n1, n

print("Numbers after swapping : ")
print("First number : ", n)
print("Second Number : ", n1)