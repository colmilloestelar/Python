import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?."
gen = len(s)-1
r = ""
x = 0
print("Welcome to pass generator v1.0 2018")
lon = int(input("How many big want your password"))

while (lon>0):
    x = random.randint(0,gen)
    r = r+s[x]
    lon-=1

print(r)
