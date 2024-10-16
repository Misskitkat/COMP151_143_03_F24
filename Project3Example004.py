"""
Code from Dr. Gross in class 004 on 10/15/2024
Good luck :)
"""

store_records = [['Market Basket', ['corn flakes', 'white bread', 'pop rocks'], [800, 1000, 100]],
                 ['Star Market', ['bagels', 'cheetos', 'coffee cake'], [850, 400, 100]],
                 ['Roche Bros', ['wings', 'apples', 'brownies'], [100, 2000, 100]]]

market_basket_record = store_records[0]
print(f"{market_basket_record[0]} has {market_basket_record[1][0]}:"
      f" {market_basket_record[2][0]}.")
print("Sell 100 items.")
market_basket_record[2][0] -= 100
print(f"{market_basket_record[0]} has {market_basket_record[1][0]}:"
      f" {market_basket_record[2][0]}.")

cornflake_amount = store_records[0][2][0]
if cornflake_amount < 100:
    print("Order more.")
else:
    print("Inventory is still adequate.")

grocery_list = []
for record in store_records:
    products = record[1]
    for product in products:
        grocery_list.append(product)

# In place of append I used concatenation of lists.
'''
grocery_list = []
for record in store_records:
    products = record[1]
    grocery_list += products
'''

print(sorted(grocery_list))