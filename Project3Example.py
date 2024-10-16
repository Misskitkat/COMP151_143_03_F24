"""
Code from Dr. Gross in class on 10/15/2024
Good luck :)
"""

store_records = [['Market Basket', ['corn flakes', 'white bread', 'pop rocks'], [800, 1000, 100]],
                 ['Star Market', ['bagels', 'cheetos', 'coffee cake'], [850, 400, 100]],
                 ['Roche Bros', ['wings', 'apples', 'brownies'], [100, 2000, 100]]]
store0 = store_records[0]
products = store0[1]
amounts = store0[2]
print(f"{store0[0]} has {products[0]}: {amounts[0]}.")
print("Sell 100 items.")
# amounts[0] = amounts[0] - 100
amounts[0] -=  100
print(f"{store0[0]} has {products[0]}: {amounts[0]}.")

if amounts[0] < 100:
    print("Order more.")
if amounts[0] >= 100:
    print("Inventory is still adequate.")

grocery_items = []
for record in store_records:
    products = record[1]
    for product in products:
        grocery_items.append(product)

'''
grocery_items = []
for i in range(len(store_records)):
    for product in store_records[i][1]:
        grocery_items.append(product)
'''

print("Featured products are:")
print(sorted(grocery_items))