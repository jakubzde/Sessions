import random

numbers = [1,2,3,4,5]
print(numbers)

count = 0
while count <= 9:
    numbers.append(random.choice(range(5,20)))
    count += 1

print(numbers)

#def greet(name):
    #"""
    #Input: none
    #This function just prints "Hello, <name>."
    #"""
    #print("Hello, ", str(name).capitalize())

#greet("jakub")

def sum_and_multiply(n1,n2,m):
    """
    :parameter n1: number for addition 1
    :parameter n2: number for addition 2
    :parameter m: multiplier
    :return: prints (n1+n2)*m

    Adds n1 and n2 and multiplies the result by m.
    """
    print((n1+n2)*m)

sum_and_multiply(1,2,3) # We do not use print() cuz the function already has it in itself.

def sum_and_multiply1(n1,n2,m):
    """
    :parameter n1: number for addition 1
    :parameter n2: number for addition 2
    :parameter m: multiplier
    :return: prints (n1+n2)*m

    Adds n1 and n2 and multiplies the result by m.
    """
    return (n1+n2)*m

result = sum_and_multiply1(1,2,3) # Here we need to use wrint cuz it is not in the function.
print(f"(1+2)*3-4 = {result-4}") # This allows us to furter work with it.

def introduce(name):
    """
    :param name: a regular string
    :return: prints the name
    """
    print("The name is:", name)

def bond(first_name = "james", last_name = "bond"):
    """
    :param first_name: first name, default "james"
    :param last_name: last name, default "bond"
    :return: returns a cool introduction
    """
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return last_name+","+" "+first_name+" "+last_name

introduce(bond())