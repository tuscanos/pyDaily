# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

sentence = input("Enter a sentence with letters and digits: ")

letters = 0
digits = 0
for s in sentence:
    if s.isalpha():
        letters += 1
    elif s.isdigit():
        digits += 1

print("LETTERS ", letters)
print("DIGITS ", digits)

