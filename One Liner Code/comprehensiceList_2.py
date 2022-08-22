# List comprehension using “for” and “if”
n = int(input("Enter number to generate a range of numbers from 0 to end point: "))
tempList = [number for number in list(range(0, n+1)) if number % 2 == 0]
print("Even number list:\t", tempList)