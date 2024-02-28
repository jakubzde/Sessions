print("Here will be the contents of the file:")
num_aliens = 0
with open("x-files.txt", "r") as f: # "r" for read
    # inside here the f file is open for reading
    #print(f.read()) # this line will give us what is in the file (we can't use this line with the comand below)
    for line in f:
        num_aliens += line.lower().count("alien") # it puts all in lowercase and then count it

# once I am out, the file is closed
print("The word alien shows up", num_aliens,"time(s) in the file.")