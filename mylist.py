
Pets = []

def builder(Pets):
    
    
    print("let's build a list of animals you like")

    for x in range(0,6):
 
        animal = str(input('type your animal name and hit enter:\n'))
        Pets.append(animal)

builder(Pets)

print(Pets)
