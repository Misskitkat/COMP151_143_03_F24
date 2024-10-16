"""
This is a summary of what we did in week 3. Examples from the thinking tasks as well as others from the book.
I will put print statements in sections so that when you run the code it will tell you what section you are in.
Try to predict what is going on mentally.
< click on the number to create a break point where you can run the code until that point.
In the console there is a little step over button if you have one or multiple break points.
"""
import random
import math

print("\tSection 1")

pokemon = ["Lucario","Flygon", "Empoleon", "Luxray", "Corvknight"]
print(type(pokemon))
print(type(pokemon[1]))
print(type(len(pokemon)))
print(f"The length of the pokemon list is: {len(pokemon)}.")
print(f"The length of the pokemon {pokemon[0]} is {len(pokemon[0])}.")
print()
print(sorted(pokemon))
print(sorted(pokemon, reverse = True))
print(pokemon)

print("\n\tSection 2")

number_list = [23,4,51,0,1]
print(number_list)
print(sorted(number_list))
print(sorted(number_list, reverse = True))

print("\n\tSection 3")

print(pokemon[0])
print(pokemon[1])
print(pokemon[2])
print(pokemon[3])
print(pokemon[4])
print(pokemon[-1])
print(pokemon[-3])
# showing what you can do to index, negatives start from the right side and count that left, does not start at 0

print("\n\tSection 4")

pokemon[1] = "Umbreon"
pokemon[3] = "Absol"
print(pokemon)
pokemon.append("Luxray")
pokemon.append("Flygon")
print(pokemon)
pokemon.insert(4, "Meowscarada")
print(pokemon)
pokemon.insert(5, "Incineroar")
print(pokemon)
del pokemon[-1]
print(pokemon)
chosen_pokemon = pokemon.pop(1)
print(chosen_pokemon)
print(pokemon)
pokemon.remove('Incineroar')
print(pokemon)
# this is how you can change the elements of the list, and add more elements to the list
# what is the visible difference between pop and remove? pop can be returned, stored, but by index, removed is by the value and cannot be stored ina variable like pop


print("\n\tSection 5")

print(pokemon)
print(pokemon[0])
print(pokemon[1])
print(pokemon[2])
print(pokemon[random.randrange(len(pokemon))], "was randomly chosen")
# creating a list requires the [], you can use '' or "" but will print '', then use the [] to index into the list to grab the element stored there

print("\n\tSection 6")
print(f"{pokemon[0]} is one of my favorites")
print(f"{pokemon[1]} is one of my favorites")
print(f"{pokemon[2]} is one of my favorites")
print(f"{pokemon[3]} is one of my favorites")
