#Q1
print(type(2+3))
print(type(6/2))
print(type(5 or 6))
print(type(print()))
print(type(print(2*2)))
print(type("abc".find))
#print(type("bubu"*(4/2))) => print(type("bubu"*int((4/2)))) <= would be a string
print(type(["abc", 2]))
print(type((2)))

#Q2
x = [1,2,3]
x.append("John")
print(x)

#print("bubu"*(4/2))

print(len(("abc", 2)))
print(2+3*2**2)

#Q3
a = 2
b = 3
c = "abc"
print(a, b, c)
print(a, b, c, sep=",")
a += 2
a == 5
print(a)
print(c*(a-b))
d = c.find("b") # The .find() method just returns the index/position of the first occurance of the given character
print(d)
print(d and b)
print(d == True)
e = str(a) + str(b) + str(c) + str(d)
print(e) # 43abc1
print(e[1::2]) # 3b1
print(e+e[::-1]) # 43abc1<reversed 43abc1>

#Q4
def b_words(file_name):
    """
    :parameter file: file_name
    :return: all the 3-letter words in the file that statr with "b"
    """
    punctuation = ",.!?\n"
    with open(file_name, "r") as file:
        for line in file:
            for p in punctuation:
                line = line.replace(p, " ")
            words = line.split(" ")
            for word in words:
                if (word.startswith("b") or word.startswith("B")) and len(word) == 3:
                    print(word)

b_words("midterm_ex_1.txt")

#Q5
def divisors(int):
    """
    Takes an intiger and returns its divisors.
    :parameter: integer
    """
    num = 1
    while num < int:
        if int % num == 0:
            print(num)
        num += 1
    print(num)

divisors(28)

#Q6
try:
    multiple_of_6 = input("Please write a multiple of 6. ")
    multiple_of_6 = int(multiple_of_6)

    while multiple_of_6 % 6 != 0:
        print("That is not multiple of 6.")
        multiple_of_6 = input("Please write a multiple of 6. ")
        multiple_of_6 = int(multiple_of_6)
    
    print("Thank you for writing a multiple of 6.")

except ValueError:
    print("I am sorry that was not a valid number.")

