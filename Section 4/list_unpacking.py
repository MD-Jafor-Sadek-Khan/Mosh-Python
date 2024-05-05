"""List Unpacking"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

first, *others, second_last, last = numbers

print(first, others, second_last, last)
