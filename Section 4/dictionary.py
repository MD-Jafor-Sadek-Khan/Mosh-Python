"""dictionary"""

point = {"x": 1, "y": 2}
point = dict(x=1, y=2)

point["x"] = 7
point["z"] = 12

del point["z"]

if "x" in point:
    print("yes")

print(point.get("a", -1))

for key, value in point.items():
    print(key, " => ", value)
print(point)
