from sys import argv

script_name , two, three, four,fifth = argv

print("script name ", script_name)
print("first number ", two)
print("second number ", three)
print("Thrid number ", four)

fifth = input(f"Is realy the {fifth} your name? ")

print(f"{fifth} I guess it is")