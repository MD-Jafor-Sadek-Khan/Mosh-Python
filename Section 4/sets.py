"""Sets"""

first_set = set([1, 1, 2, 3, 4])

second_set = {1, 5}

print(first_set | second_set)
print(first_set & second_set)
print(first_set - second_set)
print(first_set ^ second_set)

if 1 in first_set:
    print("yes")