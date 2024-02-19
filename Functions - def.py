def greet(): # we are defining a function called greet
    # below is a description of the function we create (does not change anything)
    """
    This is a basic function used for teaching.
    It just prints two lines of text.
    :return: None
    """
    print("Hello, world!")
    print("Bye, world!")

greet() # we also have to call the function for it to appear
a = greet()
print(a) # the return is none

def sum_3_numbers(a, b, c):
    """
    This function sums 3 numbers
    :param a: the first number
    :param b: the second number
    :param c: the third number
    :return: the sums of these 3 numbers
    """
    return a + b + c

b = sum_3_numbers(10,20,30)
print(b)

def operation_3_numbers(a, b, c): # if we write "def operation_3_numbers(a, b, c=0):" it will autofill "c" as 0 when it is left empty
    """
    This function operates 3 numbers
    :param a: the first number
    :param b: the second number
    :param c: the third number
    :return: the operates these 3 numbers
    """
    return a * b + c

c = operation_3_numbers(10,20,30) # parameters taken by position
print(c)
c1 = operation_3_numbers(a=10,c=20,b=30) # parameters taken by names (not "abc" but "acb")
print(c1)

def read_3_numbers():
    """
    This function reads 3 numbers from the user
    :return: the 3 numbers
    """
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    c = int(input("Enter the third number:"))
    return a, b, c

a, b, c = read_3_numbers()
print(operation_3_numbers(a,b,c))
