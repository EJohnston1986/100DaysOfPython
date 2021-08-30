import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

listLength = len(names) -1
randPerson = random.randint(0, listLength)

print(f"{names[randPerson]} has to pay the bill")


