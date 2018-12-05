# -*- coding: utf-8 -*-

def budgeting(budget, products, wishlist):
    """
    Given an integer budget, a dictionary products (name: price) and a dictionary wishlist (name: amount), checks if the items in the wishlist fit the budget.
    If not, removes the cheapest items from the wishlist until it fits the budget.
    """
    total = 0
    for item in wishlist:
        total += wishlist[item] * products[item]
    
    if total <= budget:
        return wishlist
    else:
        lowest_item = ""
        lowest_val = max(products.values())
        
        while total > budget:
            if lowest_item not in wishlist:
                lowest_val = max(products.values())
                for item in wishlist:
                    if products[item] <= lowest_val:
                        lowest_val = products[item]
                        lowest_item = item
            
            if wishlist[lowest_item] == 1:
                wishlist.pop(lowest_item)
            else:
                wishlist[lowest_item] -= 1
            
            total -= lowest_val
    
    return wishlist

#Tests
print(budgeting(1000, {'ps4': 350, 'smartphone': 400, 'jacket': 40,'pc': 600, 'glasses': 75}, {'ps4': 1, 'smartphone': 1, 'pc': 1}))
print(budgeting(1500, {'xbox': 250, 'smartphone': 500, 'jeans': 50, 'pc': 600, 'glasses': 100}, {'glasses': 3, 'jeans': 2, 'pc': 1, 'xbox':1}))
print(budgeting(1200, {'xbox': 250, 'smartphone': 500, 'jeans': 50, 'pc': 600, 'glasses': 100}, {'glasses': 3, 'jeans': 2, 'pc': 1, 'xbox':1}))
print(budgeting(750, {'nintendo': 100, 'mouse': 20, 'hoodie': 45, 'backpack': 30, 'tv': 300}, {'nintendo': 1, 'mouse': 1, 'hoodie': 4, 'tv': 2}))