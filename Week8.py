"""
This is a summary of what we did in week 8. Examples from the thinking tasks as well as others from the book.
I will put print statements in sections so that when you run the code it will tell you what section you are in.
Try to predict what is going on mentally.
< click on the number to create a break point where you can run the code until that point.
In the console there is a little step over button if you have one or multiple break points.
"""

print("\tSection 1")

weights={"A": 4.0, "B": 3.0, "C": 2.0}
print(weights["C"])
print(weights.get('C'))
# see how we can index using the key and we get the value
# dictionaries are like lists but you choose the name of the index instead of it being from 0-#

haitian_creole = {'vandredi': 'friday',
                  'samdi':'saturday'}
haitian_creole['dimanch'] = 'sunday'
print(haitian_creole)

credits = {}
credits['MATH 161E'] = 4
print(credits)
# you can add to a dictionary by creating a key and setting that equal to a value even when the d



print("\n\tSection 2")

# credits.append(3)
# this will give an error because you cannot append to a dictionary
# instead you can do this:
inventories = []
market_basket = {'corn flakes': 800, 'white bread': 1000,
                 'pop rocks': 100}
star_market = {'bagels': 850, 'cheetos': 400,
               'coffee cake': 100}
roche_bros = {'wings': 100, 'apples': 2000,
              'brownies': 100}

inventories.append(market_basket)
print(inventories)
# this way there is a dictionary in a list
# the opposite works too, lists inside of a dictionary

friends = {}
bob = [21, 'green', 'boston']
kara = [23, 'purple', 'middleboro']
alex = [20, 'blue', 'plymouth']
friends['bob'] = bob
friends['kara'] = kara
friends['alex'] = alex
print(friends)
# you can use variables but you can also do it a different way

friends['bob'].append('MA')
print(friends)
# this way you can store multiple values for a key and access them by indexing
# but you do not index into a dictionary, only into lists

print("\n\tSection 3")

# using for loops with dictionaries
squares = {}
for x in range(5):
    squares[x] = x**2
print(squares)