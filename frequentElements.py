# Calculate frequent elements
import random
numbers = [1,212,11,1,21321,4,564,11,1,1,1,22,5]
print("List")
print(numbers)
most_frequent_element = max(set(numbers), key=numbers.count)
print("Most frequent number:\t",most_frequent_element)