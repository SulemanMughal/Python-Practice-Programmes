# Combine nested lists to a single list
n = int(input("Enter number to generate a range of numbers from 0 to end point: "))
tempList = [item for sublist in range(0, n+1) for item in range(sublist+1, 0, -1)]
print("Generated List:\t", tempList)