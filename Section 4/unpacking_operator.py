"""unpacking_operator"""

first = [1, 2]
second = [2, 3, 4]
combined = [*first, 6996,*second]
print(combined)

first = {"x": 10}
second = {"x": 1, "y": 20}
combined = {**first,"z":12, **second}
print(combined)
