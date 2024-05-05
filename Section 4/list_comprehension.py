"""List Comprehension"""


products = [
    ("product1", 100),
    ("product0", 300),
    ("product3", 200),
]

prices = [product[1] for product in products]

filtered = [product for product in products if product[1] >= 200]

print(prices, filtered)
