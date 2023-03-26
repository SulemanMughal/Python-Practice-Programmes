# Nested comprehensive list
listA = []
x = int(input("Enter number of elements for list: "))
i = 0
while i < x:
    listA.append(int(input("Enter " + str(i+1)  + " element for list: ")))
    i = i+1

print("List")
print(listA)
print("Nested comprehensive list")
listA = [[num] for num in listA]
print(listA)