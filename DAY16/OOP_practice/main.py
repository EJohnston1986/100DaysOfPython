import turtle
from prettytable import PrettyTable
import another_module
from turtle import Turtle, Screen

table = PrettyTable()
print(table)

table.add_column("Pokemon Name",
                 ["Pikachu","Charizard"],"l")
table.add_column("Type",
                 ["Electric", "Fire"],"l")
print(table)