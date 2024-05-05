"""generator"""

from sys import getsizeof

# generator
values = (x*2 for x in range(5000000))
print(getsizeof(values))

# list
values = [x*2 for x in range(5000000)]
print(getsizeof(values))

# set
values = {x*2 for x in range(5000000)}
print(getsizeof(values))

# dictionary
values = {x: x*2 for x in range(5000000)}
print(getsizeof(values))
