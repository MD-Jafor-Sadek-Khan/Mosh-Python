"""sorting items"""

products = [
    ("product1", 100),
    ("product0", 300),
    ("product3", 200),
]


def sort_items(item):
    """call back function for sorting list"""
    return item[0]


products.sort(key=sort_items)
print(products)
