# Longest word from a sentence
sentence = input("Enter sentence: ")
print(max(sentence.split(" "), key=len))