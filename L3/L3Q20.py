# Question 20
# Level 3
#
# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

class MyGenerator():

    def __init__(self, n):
        self.num = n

    # This can be any function name
    def iter(self):
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
it = g.iter()       # This gives generator object
print(it)

for i in it:        # for loop calls it.next() method to get the next value
    print(i)
