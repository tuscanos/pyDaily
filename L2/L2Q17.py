# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. 
# The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

netAmount = 0

print("Enter transaction log: ")
while True:
    s = input()
    if not s:
        break
    
    data = s.split(" ")
    operation = data[0]
    amount = int(data[1])

    if data[0] == 'D':
        netAmount += amount
    elif data[0] == 'W':
        netAmount -= amount

print("You have: ", netAmount)
