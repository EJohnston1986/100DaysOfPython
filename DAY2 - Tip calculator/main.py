# Tip calculator

print("Welcome to the tip calculator")

bill = float(input("What was the total bill?"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15"))
numPeople = int(input("How many people split the bill?"))

totalBill = bill + (bill / 100 * tip)
splitBill = "{:.2f}".format(totalBill/numPeople)

print(f"Each person should pay: £{splitBill} ")


