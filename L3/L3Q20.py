# Question 20
# Level 3
#
# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

class MyGenerator():

    def __init__(self, n):
        self.num = n

    # This can be any function name
    def __iter__(self):     # This allows constant iteration on the object
        n = self.num
        while n > 0:
            if n % 7 != 0:
                n -= 1
                continue
            else:
                yield n
                n -= 1
        print("Done")


g = MyGenerator(100)
# it = g.iter()       # This gives generator object, this is not needed
# print(it)

for i in g:        # for loop calls it.next() method to get the next value
    print(i)

# Iteration does not run out of values when we use above class defination with __iter__
# below values works because of class __iter__ method. otherwise it would be stopIteration error

for i in g:        # for loop calls it.next() method to get the next value
    print(i)
