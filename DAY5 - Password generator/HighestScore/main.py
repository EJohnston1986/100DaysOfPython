# 🚨 Don't change the code below 👇
studentScores = input("Input a list of student heights ").split()
for n in range(0, len(studentScores)):
  studentScores[n] = int(studentScores[n])
# 🚨 Don't change the code above 👆

highestScore = 0
for score in studentScores:
  if score > highestScore:
    highestScore = score

print(f"The highest score is: {highestScore}")