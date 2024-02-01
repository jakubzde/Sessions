text = "Aaaaaaa5718bc"
print(text.lower())
print(text.isidentifier()) #True
print("1".isidentifier()) #False
print("1a".isidentifier()) #False
print("a".isidentifier()) #True
print("a1".isidentifier()) #True
print(text.count("a")) #Counts the occurences of a character in an object
print(text.lower().count("a"))
print("jkkkjak".count("a"))
print("anna".replace("na","we"))
print("anaana".find("ana", 1)) #?
print("bbbabbbabbbabbbabbb".split("a")) #Splits a string where the key character is
print("This is a string and I want the words".split(" "))
sentence = "Hello, kind-sir; how may! I be of service today?"
punctuation = ".,;?!-"
#sanitize the sentence
for p in punctuation:
    sentence = sentence.replace(p, " ") #replace the punctuation with nothing
print(sentence)
sentence = sentence.replace("  ", " ") #replace double spaces for single spaces
#split the sentence into words
words = sentence.split(" ")

name = "John"
second_name = "Bob"
print(f"Hi, {name} how are you? My name is {second_name}.")
name = "Jane"
second_name = "Mary"
print(f"Hi, {name} how are you? My name is {second_name}.")