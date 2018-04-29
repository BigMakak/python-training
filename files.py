from sys import argv
#Assigns the argumetns passed with the running of the script
script , filename = argv

#Opens the file with the filename that is passed was an argumets
file = open(filename)

print(f"Wheres your file name {filename}")
print(file.read())

print("Type the name of another file to read.")
file2_name = input(" > ")

#Asigns the file object with the name of the file with the input wanted.
file2 = open(file2_name)

print(file2.read())