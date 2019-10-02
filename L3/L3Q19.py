# Question 19
# Level 3
#
# Question:
# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers.
# The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

from operator import itemgetter, attrgetter

data = []
print("Enter name, age, height: ")
while True:
    in_data = input()
    if in_data:
        data.append(tuple(in_data.split(',')))
    else:
        break

# TODO: Check if lambda can be used here
data = [(name.strip(), int(age.strip()), int(height.strip())) for name, age, height in data]
print("originalList: ", data)

# sortByAge = sorted(data, key=lambda d: d[1])
# print("Sorted By Age: ", sortByAge)
#
# sortByName = sorted(data, key=lambda n: n[0])
# print("Sorted By Name: ", sortByName)
#
# sortByHeight = sorted(data, key=lambda h: h[2])
# print("Sorted By Height: ", sortByHeight)


sortUsingItemgetter = sorted(data, key=itemgetter(1, 2))
print("sortUsingItemgetter: ", sortUsingItemgetter)

# This will error here, as we do not have named attribute
# sortUsingAttrgetter = sorted(data, key=attrgetter('name'))
# print("sortUsingAttrgetter:", sortUsingAttrgetter)

sortUsingItemgetter_name_height = sorted(data, key=itemgetter(0, 2))
print("sortUsingItemgetter_name_height: ", sortUsingItemgetter_name_height)

sortUsingItemgetter_age_height = sorted(data, key=itemgetter(1, 2))
print("sortUsingItemgetter_age_height: ", sortUsingItemgetter_age_height)

sortUsingItemgetter_name_age_height = sorted(data, key=itemgetter(0, 1, 2))
print("sortUsingItemgetter_name_age_height: ", sortUsingItemgetter_name_age_height)

# My example:
# Tom,19,80
# John,20,90
# Shonal, 10, 34
# Raymond, 33, 129
# Tom, 20, 99
# Tom, 19, 40