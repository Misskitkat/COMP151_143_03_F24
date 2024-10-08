"""
This is a summary of what we did in week 1. Examples from the thinking tasks as well as others from the book.
I will put print statements in sections so that when you run the code it will tell you what section you are in.
Try to predict what is going on mentally.
< click on the number to create a break point where you can run the code until that point.
In the console there is a little step over button if you have one or multiple break points.
"""

print("\tSection 1")
pokemon = ["Lucario","Flygon", "Empoleon", "Luxray", "Corvknight"]
pokemon.reverse()
print(pokemon)
# this reverses the order
pokemon.sort()
print(pokemon)
# this sorts it based on Unicode (along the same lines as ASCII but slightly different)
pokemon.sort(reverse = True)
print(pokemon)
# this sorts it in reverse order
print(pokemon * 2)
# creates a list of the same list and combines it that many times
# try to predict these next few on your own before checking
print("\n\tSection 2")
print(pokemon[2])
# grabs the element at that index and returns it
print(pokemon[0:2])
# returns a list of elements from 0-2 or indices 0 and 1
print(pokemon[2:4])
# same as 0:2 but from 2:4 so indices 2 and 3 are returned
print(pokemon[:4])
# the : is a range, so from nothing to a number meaning it will return 0-4
print(pokemon[:-2])
# this means it will return everything but the last 2
print("Pokemon"[-2:])
print("Pokemon"[1:5])
print("Pokemon"[3:])
print("Pokemon"[:-2])
# the above 4 are the same as the list but with a string, a string is just a condensed list of chars or one element strings

print("\n\tSection 3")
number_list = [3,40,31,80,5]
print(max(number_list))
print(min(number_list))
print(sum(number_list))

characters_list = ['3', 'a', 'A', '0', '(', '7']
# why is the 'a' greater than everything else? like before with the unicode, every character has a number attached and
# 'a' has a greater number than everything else in this list
print(max(characters_list))

print("\n\tSection 4")
print("Making copies of a list.")
pokemon_list_2 = pokemon
# why does this not work?
print(f"pokemon: {pokemon}")
print(f"pokemon: {pokemon_list_2}")
# they come out the same right?
pokemon.append("Umbreon")
print(f"pokemon: {pokemon}")
print(f"pokemon: {pokemon_list_2}")
# they still came out the same right?!
# instead of setting them equal, do this
pokemon_list_2 = pokemon[:]
# trust me at the moment they are the same
pokemon.append("Meowscarada")
print(f"pokemon: {pokemon}")
print(f"pokemon: {pokemon_list_2}")
# now they are different right?
# you can manipulate one list without affecting the other one like this, when you set them equal
# without [:] you are just pointing two variables to the same list of elements

print("\n\tSection 5: INCLUDING LOOPS")
chosen_pokemon = ["Lucario","Flygon", "Empoleon", "Luxray", "Corvknight"]
for pkmn in chosen_pokemon:
    print(pkmn)
    # we can loop through the list element by element and print out each element
print("\nOR THIS WAY\n")
for i in range(len(chosen_pokemon)):
    print(chosen_pokemon[i])
    # doing the same thing as the loop above but going index by index instead of by element
print("\nSAME THING\n")
# this is also showing you how indents matter, the extra prints outside of the loop do not loop, only everything inside the loop repeats
print("\n\tSection 6")
grades = [4.0, 3.0, 4.0, 3.0, 2.0,]
print(f'Grades for {len(grades)} classes:')
for grade in grades:
    print(f'The grade is: {grade}')

print()
for letter in "AEIOU":
    print(letter)
print("Vowels\n")
# just like before how I said that a string is like a condensed list, you can loop through a string element by element

print()
for i in range(10):
    print(i)
print("starts at 0 and goes until 9\n")
for i in range(2,9):
    print(i)
print("starts at 2 and cant go to 9\n")
for i in range(0,11,2):
    print(i)
print("goes up to 10 by 2\n") # this is called stepping
for i in range(0,10,2):
    print(i)
print("cannot go up to 10, still going by 2\n")
print(range(5))
print(type(range(5)))
print(list(range(5)))

print("\n\tSection 7")
for i in range(3):
    print("Go Bears!")
    # this prints go bears 3 times
print()
mascot = "Bears"
for i in range(3):
    print(f"Go {mascot}!!!")
    # shows another way to do this

print()

print("\n\tSection 8")
number = 4
for i in range(number):
    print(i)
    """ here we can see that it is going to print
        0
        1
        2
        3
        and not 0 1 2 3 , there is a newline character at the end of each print statement"""
print()
count = 2
count = count + 1
for i in range(4):
    print(count)
    # we can see here how we can increment a number, just set it equal to itself with + 1
print()
for i in range(3):
    print(i)
    print("Blastoff!")
    # here we can see that after every number blastoff is printed, which is not the most effective way to use a countdown
print()
# instead do this
for i in range(5):
    print(i)
print("Blastoff!!!")
# this way you are counting up to it instead of counting up and immediately saying it
print()
# what if you wanted to count down?
for i in range(4):
    print(3-i)
print("Blastoff!!")
# this counts down instead of counting up

print()
# there is a way to refactor this though
number = 6
for i in range(6):
    print(number-1-i)
print("Blastoff!!!!!")
# this way we can use the same variable for both and then also change that variable instead of hard coding it in.