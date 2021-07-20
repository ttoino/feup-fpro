def budgeting(budget: int, products: dict, wishlist: dict):
    while budget < sum([wishlist[i] * products[i] for i in products if i in wishlist]):
        products = {i: products[i] for i in products if i in wishlist}
        wishlist[min(products.items(), key=lambda x: x[1])[0]] -= 1
        wishlist = {k: v for k, v in wishlist.items() if v > 0}

    return wishlist