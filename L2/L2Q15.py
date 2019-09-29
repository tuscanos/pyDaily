# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

d = input("Enter number: ")

addCount = 0

for i in range(1, 5):
    addCount += int(str(d) * i)

print(addCount)