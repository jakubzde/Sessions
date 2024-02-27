num = 0
count = 0
while num <= 19:
    if num % 3 == 0:
        count += 1
        num += 1
    num += 1
    
print("Numbers divisible by 3", count)