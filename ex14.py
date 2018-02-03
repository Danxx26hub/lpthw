#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from sys import argv


script, user_name = argv

prompt = '>'


print(f"hi {user_name} my name is {script}")

print("I would like to ask you a few questions.")


print(f"do you like me {user_name}?")

likes = input(prompt)

print(f"where do you live {user_name}?")

lives = input(prompt)

print("what kind of computer do you have?")

computer = input(prompt)

print(f"""alright, so you said {likes} about liking me.
           you live in {lives}. not sure where that is.
           And you have a {computer}. Nice. 
    """)


