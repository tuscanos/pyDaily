# Question:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9


# l = input("enter comma separated numbers: ").split(',')
# ll = [int(y) for y in l]
#
# oddlist = [x for x in ll if x %2 != 0]
#
# print(oddlist)



values = input("enter comma separated numbers: ")

# ll = [int(y) for y in l]

oddlist = [x for x in values.split(',') if int(x) %2 != 0]

print(oddlist)