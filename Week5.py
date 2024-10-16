"""
This is a summary of what we did in week 5. Examples from the thinking tasks as well as others from the book.
I will put print statements in sections so that when you run the code it will tell you what section you are in.
Try to predict what is going on mentally.
< click on the number to create a break point where you can run the code until that point.
In the console there is a little step over button if you have one or multiple break points.
"""
import math
print("\tSection 1")

print(3 > 4) # what does false mean?
print(4 > 3) # what about true

x = 10
print(x > 2)

print(x == x)
print(5==5)
print(x == 9)

print(math.pi == 3)

print(7 < 7)
print(7 <= 7)
print()
print("Notice the double equals? The double equals is comparison only while the single is assigning values.")

print("\n\tSection 2")

print(type(3>4))
print(type(True))
print(type("False"))
print("Notice the title case, bools are True and False not true and false.")

print("\n\tSection 3")

name = "Da'Shaun"
print(name == "Da'Shaun")

print("laura"<"tina")
print("laura"<"Tina")

print("\n\tSection 4")

my_age = 22
sibling_age = 20
print(my_age >= 21 and sibling_age >= 21) # and 21
print(my_age >= 21 or sibling_age >= 21) # or 21
print(my_age >= 18 and sibling_age >= 18) # and 18
print(my_age >= 18 or sibling_age >= 18) # or 18

print("\n\tSection 5")

name = "Dr. Black"
cs_professor = True
history_professor = False
print(name == "Dr. Black" or cs_professor)
print(not(history_professor))

print((3 < 4) and (5 < 3))
print(True and False)
print((len([1, 1, 0, 1, 0]) == 5) and (3 < 7))

print((len("Howdy") == 5) and (5 < 3))
print((3 < 4) and ("Laura"[2] == "u"))

print("\n\tSection 6")

print("\nIf statements!!!")

age = 19
if age >= 21:
    print("You can be admitted to the concert.")

number_siblings = 1
if number_siblings > 0:
    print("You have siblings!")
if number_siblings > 1:
    print(f"Do you enjoy spending time with your {number_siblings} siblings?")
if number_siblings == 1:
    print("Do you enjoy spending time with your 1 sibling?")
if number_siblings == 0:
    print("Do you enjoy being an only child?")
if number_siblings < 0:
    print("ERROR")
print("Let's talk about your cousins.") # what would happen if you changed the number of siblings?

student = 'Matthew'
group = ['Michael', 'Jamal', 'Will']
if student in group:
    print('The student is in the group.')
if not(student in group):
    print('The student is not in the group.')


