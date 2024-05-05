"""while loop"""
command: str = ""
print("\nType \"quit\" to quit the console\n")
while command.lower() != "quit":
    command = input("Input: ")
    print("Echo", command)
