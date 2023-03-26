# Merge two sets

n = int(input("Enter number to generate first set of numbers from 0 to end point: "))
setA = {x*x for x in range(0,n+1) }
print("First  set:\n", setA)
n = int(input("Enter number to generate second set of numbers from 0 to end point: "))
setB = {x*x for x in range(0,n+1) }
print("Second  set:\n", setB)
setA.update(setB)
print("Merge both sets\n")
print(setA)