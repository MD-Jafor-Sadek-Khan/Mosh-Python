"""adding_or_removing_from_list"""

letters = ["a", "b", "c", "d"]

# add
letters.insert(0, "-")
letters.append("e")

# remove
letters.pop()
letters.pop(0)
del letters[:2]
letters.remove("c")
letters.clear()
print(letters)
