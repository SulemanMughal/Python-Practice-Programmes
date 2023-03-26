# Dictionary comprehensive

n = int(input("Enter number to generate a dictionary of numbers from 0 to end point: "))
tempList = {x:x*x for x in range(0,n+1) }
print("Generated Dictionary:\n", tempList)