#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from sys import argv


script, filename = argv 

print(f"We're going to erase {filename}.")

print("if you don't want that, hit CTRL-C (^c).")

print("if you do want that, hit RETURN key.")

input("?")

print("opening the file ........")

target = open(filename, 'w')

print("Truncating the file. Goodbye!")

target.truncate()

print("now I'm going to ask you for three lines.")

line1 = input("line 1: ")

line2 = input("line 2: ")

line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")

print("And finally , we close it.")
target.close()
