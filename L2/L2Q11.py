# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

b = input('Enter comma separated 4 digit binary numbers: ').split(',')

# number_b = [int(a) for a in b]
mylist = []

for i in b:
    inti = int(i,2)
    if not inti % 5:
        mylist.append(i)

# print(mylist)
print(','.join(mylist))