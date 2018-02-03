#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from sys import argv


script, = argv

print("the name of the script is:", script)

ans = input("Please confirm the name matches by typing in the name\n")

if ans == script:
    print("yes they match!")
else:
    print("sorry that is not match")
