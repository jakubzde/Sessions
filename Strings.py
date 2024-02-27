hi = "Hello!"

for x in reversed(hi):
    print(x)

print(hi[::-1])

print("e" or "o" in hi)

print(hi.find("e"))

s = "http://google.com and then there could be http://yahoo.com or even a website like http://bbc.co.uk"
start = 0
while True:
    start = s.find("http://", start)
    if start == -1:
        break
    end = s.find(" ",start)
    if end == -1:
        print(s[start:])
        break
    print(s[start:end])
    start = end

template = "%s I have seen %d %s."
print(template % ("Today", 3, "dogs"))
print(template % ("On Monday", 7, "cats"))

hi = "Hello"
who = "World"
print((3 * (hi + " ") + 5 * (who + ",")))
print((3 * (hi + " ") + 5 * (who + ",")).replace(","," "))
print((3 * (hi + " ") + 5 * (who + ",")).replace(","," ").split(" "))

r = "racecar"
r1 = r[::-1]
print(r, r1)
print(r == r1)

punctuation = ".,!?\n"
a = input("Your sentence: ")
a = a.lower().replace(" ", "")
a1 = a[::-1]
a1 = a1.lower().replace(" ", "")

for x in punctuation:
    a = a.replace(x, "")
    a1 = a1.replace(x, "")

if a == a1:
    print("The sentence is a palindrome.")
else:
    print("The sentence is not a palindrome.")