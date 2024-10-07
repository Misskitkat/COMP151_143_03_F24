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

