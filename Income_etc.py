income = input("What is your gross income? ")
income = int(income)
n_child = input("How many children do you have? ")
n_child = int(n_child)

if income < 1000:
    result = 0.10
elif (income > 1000) and (income < 2000):
    result = 0.12
elif (income > 2000) and (income < 4000):
    result = 0.14
elif (income > 4000):
    result = 0.18
else:
    result = 0

if (income < 2000):
    result1 = result-(n_child*0.01)
else:
    result1 = result-(n_child*0.01)

net = income * (1 - result1)
print(net)