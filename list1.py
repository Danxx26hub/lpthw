a = [1, 1, 3, 5, 7, 9, 13, 15, 17, 31, 71, 81,]

print(f"here is the original list: {a}")
print('\n')

num = int(input('please enter a number:'))

new_list = []

for i in a:
    if i < num:
        new_list.append(i)
        
print(new_list)