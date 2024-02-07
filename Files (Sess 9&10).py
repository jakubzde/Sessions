f = open("x-files.txt", "a") # if you write "w" it always replaces the existing text in the file with the new one; if "a" it continues on the previous text
while True:
    line = input("give me some text to put into the file:")
    if line.lower() == "stop":
        break
    f.write(line + "\n")

# we need to close the file at the end
f.close()