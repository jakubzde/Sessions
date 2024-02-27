fme = open("files_mid_ex.txt", "r")
print(fme.read())
fme.close()

#fme = open("files_mid_ex.txt", "a")
#a_text = input("What text do you want to add? ")
#fme.write("\n")
#fme.write(a_text)
#fme.close()

fme = open("files_mid_ex.txt", "w")
w_text = input("Replace the all the text with: ")
fme.write(w_text)
fme.close()