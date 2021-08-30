# Calculates two peoples compatibility

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

trueScore = 0
loveScore = 0

nameCombined = name1 + name2
nameCombined = nameCombined.lower()

t = nameCombined.count("t")
r = nameCombined.count("r")
u = nameCombined.count("u")
e = nameCombined.count("e")

trueScore = t + r + u + e
trueScore = str(trueScore)

l = nameCombined.count("l")
o = nameCombined.count("o")
v = nameCombined.count("v")
e2 = nameCombined.count("e")

loveScore = l + o + v + e2
loveScore = str(loveScore)

compatibility = int((trueScore + loveScore))

if compatibility < 10 | compatibility > 90:
    print(f"Your score is {compatibility}, you go together like coke and mentos")
elif compatibility > 39 & compatibility < 51:
    print(f"Your score is {compatibility}, you are alright together")
else:
    print(f"Your score is {compatibility}")






