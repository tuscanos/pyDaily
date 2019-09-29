# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

sentence = input("Enter a sentence with letters and digits: ")

d = {'UPPER CASE': 0, 'LOWER CASE': 0}

for s in sentence:
    if s.isupper():
        d['UPPER CASE'] += 1
    elif s.islower():
        d['LOWER CASE'] += 1
    else:
        pass

for k, v in d.items():
    print(k, v)

