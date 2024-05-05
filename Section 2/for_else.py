"""For Else"""

success: bool = False

for i in range(3):
    print("Attempt", i)
    if success:
        print("Succesful")
        break
else:
    print("Cant send message")
