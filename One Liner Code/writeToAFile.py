# Write to a file
sentence = input("Enter a sentence to write to the file: ")
print(sentence, file=open('temporary.txt', 'w'))
print("Successfully written to 'temporary.txt' file")