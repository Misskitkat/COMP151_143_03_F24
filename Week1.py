"""
This is a summary of what we did in week 1. Examples from the thinking tasks as well as others from the book.
I will put print statements in sections so that when you run the code it will tell you what section you are in.

"""
import random

# prints section 1
print("\tSection 1")
print('Hello World') # creative I know
# here you can see the difference in quotations, the single and double both end up returning to the user
# those quotations allow us to do stuff like this:
print('From some famous person: "(insert profound quote here)"')
print("it's a great quote.")
# this shows that you are able to print double when you surround it with single and vice versa

print("\n\tSection 2")
print(3*2)
print(3**2)
# this shows that the double * is exponential as its 3^2
print(3^2)
# this doesn't give you the exponential. it is bitwise xor
# not important, just know it will not give you what you expect it to (if you want to know you can dm me).

print()

print(6/2)
print(6//2)
# here you can see that there is a .0 added to the single /, that is because / is true division, and the // is floor division

print("\n\tSection 3")
# like math, you can also have a variable x = a number
x = 4
print(x)
print(x + 2)
print(x * 3)
x = x + 3
print(x / 1)
print(x // 2)
print("Let's try multiple variables")
a = 3
b = 4
print(f"a = {a} and b = {b}.")
c = a**2 + b**2
print(f"c is currently: {c} and not the actual pythagorean theorem answer")
# almost the pythagorean theorem
c = c ** .5
print(f"Now c is: {c} which is what you should get from the given a and b")
# there is a way ot make c an int, but for now the difference between a float and int does not matter.

print("\n\tSection 4")
# a variable can be more than one letter too
word = "Hello"
print(word + "world")
print(word , "world")
print(f"{word} world")
# the + shoves two words together without a space, the , adds a space, and the f string (as used above) puts the value of the variable in the {}

print("\n\tSection 5")
print(random.randrange(10))
# this will get you a number 0-9. which is 10 numbers, but you will never get 10 unless you make the range an 11 instead