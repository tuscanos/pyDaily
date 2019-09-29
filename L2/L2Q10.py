# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

words = input("Enter words: ").split(' ')

# wordst = set(words)

# words = list(set(words)).sort()
words = sorted(list(set(words)))
# words.sort()

print(' ' .join(words))

# sorted = sorted(list(set(words)))
# print(sorted(list(set(words))))