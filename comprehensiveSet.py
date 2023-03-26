# Set Comprehensive
n = int(input("Enter number to generate a set of numbers from 0 to end point: "))
tempList = {number for number in list(range(0, n+1)) }
print("Consecutive number set:\n", tempList)