"""Map Function"""


products = [
    ("product1", 100),
    ("product0", 300),
    ("product3", 200),
]

# not maintining best practice
print(sorted(list(map(lambda item: item[1], products))))


