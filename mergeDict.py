# Merge two dictionaries

n = int(input("Enter number to generate first dictionary of numbers from 0 to end point: "))
tempDictA = {x:x*x for x in range(0,n+1) }
print("First  dictionary:\n", tempDictA)
n = int(input("Enter number to generate second dictionary of numbers from 0 to end point: "))
tempDictB = {x:x*x for x in range(0,n+1) }
print("Second  dictionary:\n", tempDictB)
tempDictA.update(tempDictB)
print("Merge both dictionaries\n")
print(tempDictA)