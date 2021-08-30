#Write your code below this line 👇
def wallArea(height, width):
    area =round(height * width, 2)
    return area

def cansRequired(area, paintcan):
    cans = round(area / paintCan)
    return cans

paintCan = 5
height = float(input("What is the wall height in metres? "))
width = float(input("What is the wall width in metres? "))

area = wallArea(height, width)
cans = cansRequired(area, paintCan)

print(f"For a wall of area of {area}m^2 you will need to buy {cans} cans of paint.")





