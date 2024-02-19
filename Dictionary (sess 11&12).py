my_dict = {0:"Hello", 1:"World", 2:"Python", 3:"Programming", 4:"Language"}

print(my_dict)

my_dict2 = {"Hello":0, "World":1, "Python":2, "Programming":3, "Language":4}

my_dict[5] = "New" #Adding a pair to the dictionary
print(my_dict)

my_dict[0] = "Hi" #Changing a pair in the existing dictionary
print(my_dict)

my_dict[1] = "this", "can", "be", "a", "list" #Adding a list as a value of a single key
print(my_dict)
print(my_dict[1]) #Taking a value of a dictionary

#Not finished