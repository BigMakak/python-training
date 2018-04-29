from sys import argv

script, filename = argv

print(f"The script selected has{script}")
print(f"The file selected for testing was {filename} , to stop runnig the script press CTRL-C(^C)")

input("Ready to begin ? \r\n > ")

certificate = input("Are you sure ? \r\n > ")

print("Opening file...")
target_file = open(filename,"w")

print("Truncate file... meaning the you erased the file with the cure for AIDS..")
target_file.truncate()

print("Now you have to write your excuse to the all world what do you say?")

text_to_write = input("Excuse : ")

print("Writing to the file...")

target_file.write(text_to_write)
target_file.write(f"\n And {certificate} I did erase the cure")

print("Wanna see the file?")
input("> ")

target_file = open(filename,"r")

print(target_file.read())

print("Well nice meeting you! Bye")

target_file.close()
