
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

position.split()

column = int(position[0]) # the column element (second)
row = int(position[1])    # the row element (first)

rowChosen = map[row -1][column -1] = "X"

print(f"{row1}\n{row2}\n{row3}")