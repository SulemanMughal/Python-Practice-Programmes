# Merge two lists
listA, listB = [], []
x = int(input("Enter number of elements for first list: "))
i = 0
while i < x:
    listA.append(int(input("Enter " + str(i+1)  + " element for first list: ")))
    i = i+1
x = int(input("Enter number of elements for second list: "))
i = 0
while i < x:
    listB.append(int(input("Enter " + str(i+1)  + " element for first list: ")))
    i = i+1

print("First list:\n", listA)
print("Second list:\n", listB)
print("Merge both lists")
listA.extend(listB)
print(listA)