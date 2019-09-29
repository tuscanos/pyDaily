# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')


print('Enter comma separated numbers, hit enter once done! ')
str_list = input()\
    # .split(',')
# print(str_list)
s_list = str_list.split(',')
print(s_list)
print(list(s_list))
print(tuple(s_list))