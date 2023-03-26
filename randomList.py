# Generate a list of 'n' random numbers
import random
n = int(input('Enter number of elements in a list: '))
randomlist = random.sample(range(0, 100), n)
print(randomlist)