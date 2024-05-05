"""Lambda Function"""


products = [
    ("product1", 100),
    ("product0", 300),
    ("product3", 200),
]


products.sort(key=lambda item: item[1])
print(products)
