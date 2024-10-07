"""
This is a summary of what we did in week 2. Examples from the thinking tasks as well as others from the book.
I will put print statements in sections so that when you run the code it will tell you what section you are in.
Try to predict what is going on mentally.
< click on the number to create a break point where you can run the code until that point.
In the console there is a little step over button if you have one or multiple break points.
"""

import math
import random

print("\tSection 1")
# to copy the Week 1 file
a = 3
b = 4
print(f"a = {a} and b = {b}.")
c = a**2 + b**2
print(f"c is currently: {c} and not the actual pythagorean theorem answer")
# almost the pythagorean theorem
c = math.sqrt(c)
print(f"Here we get: {c} like in week 1, just a different method")

print("\n\tSection 2")
print("Quadratic Formula!")
a,b,c = 1,2,-1
temp = b**2 - 4*a*c
root1 = (-b + math.sqrt(temp))
root1 = root1//(2*a)
root2 = -b - math.sqrt(temp)
root2 = root2//(2*a)
# here we can use more variables to store information and break up a problem into steps
# doing the math in one line of code can get long and confusing
print(root1)
print(root2)
print(f"The values of x given the quadratic formula f(x) = {a}x^2 + {b}x + {c} are {root1} and {root2}.")

print("\n\tSection 3")
print(4*math.sqrt(64))
print(math.pi)
print(round(math.pi))
print(round(math.pi, 5))
# other examples with the math library, it will print pi until 15 places for me
print(9_001) # its over 9,000

print("\n\tSection 3")
print("Trying out more // and %.")
print(9//3)
print(10//3)
print(11//3)
print(12//3)
print(13//3)
# does it ever round up?

print()
print(9%3)
print(10%3)
print(11%3)
print(12%3)
print(13%3)
print(24%3)
# modulus takes the remainder of a division

print("\n\tSection 4")
word = ""
print(word)
word = word + "a"
print(word)
word = word + "h"
print(word)
word += "h"
print(word)
word += "!"
print(word)

print(word.upper())
print(word.title())
print(word.lower())

print("\n\tSection 5")
word_1 = "pocket    \t"
word_2 = "\n    monsters"
print(f"The first word {word_1} has trailing spaces.")
print(f"The second word {word_2} has leading spaces.")
print(f"Strip spaces from the right of word_1 to get {word_1.rstrip()}.")
print(f"Strip spaces from the left of word_2 to get {word_2.lstrip()}.")
print(word_1.rstrip(), word_2.lstrip())
print(word_1.lstrip(), word_2.rstrip())
print(word_1.strip(), word_2.strip())
# see the differences between the types of strips you can do?
# l and r make sense, left strips the white spaces off of the left side, r strips the right
# spaces, \n, \t, \r, \f count as empty spaces and will get automatically taken out
# unless...

print(word_1.strip("p"), word_2.strip().strip("m"))
# here I stripped a specific letter from the beginning of the word, and also stripped twice, word_2 had spaces taken then the 'm' taken
