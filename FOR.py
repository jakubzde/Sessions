# I want to print the multiplication table for 1 to 10 (without repetition)
for i in range (1,11):
    for j in range (i,11):
        print(f"{i} x {j} = {i*j}")
    print()