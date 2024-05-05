"""looping_over_lists"""

letters = ["a", "b", "c"]

# unpacking returned tuples to index, letters = ("index", value)
for index, value in enumerate(letters):
    print(index, value)
