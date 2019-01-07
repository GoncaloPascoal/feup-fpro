import itertools

def budgeting2(budget, products, wishlist):
    l = []

    for item in wishlist:
        for _ in range(wishlist[item]):
            l.append(item)
    
    power_set = []
    for i in range(len(l) + 1):
        power_set += list(itertools.combinations(l, i))
    
    costs = []
    for s in power_set:
        cost = 0
        for item in s:
            cost += products[item]
            if cost > budget:
                cost = 0
                break
        costs.append(cost)
    
    greatest = costs.index(max(costs))

    new_wishlist = {}
    for item in power_set[greatest]:
        if item in new_wishlist:
            new_wishlist[item] += 1
        else:
            new_wishlist[item] = 1

    return new_wishlist