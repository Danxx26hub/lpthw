#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import sqlite3

prompt = '>'

db = sqlite3.connect('db1.db')

cursor = db.cursor()

cursor.execute('''SELECT ID, NAME, ACCESS, BUILDING FROM users''')

# user1 = cursor.fetchone()

#print('printing name of first user in database')
#print(user1[1])

print('to see all records press 1, to a new record press 2, to exit press 3')
print(prompt)
a = input(str())

if a == '1':

    all_rows = cursor.fetchall()

    for row in all_rows:
        print('{0} : {1} : {2} : {3}'.format(row[0], row[1], row[2], row[3]))

#elif a == 'n':
#    print('thank you, would you like to add a user?')
    
    print(prompt)

    a = input(str())



elif a  == '2':
    print('Please enter users ID:')
    print(prompt)
    #  id = None
    id  = int(input())

    print('Please enter users name:')
    print(prompt)
    name1 = None
    name1 = input(str())


    print('Please enter users Access type (admin, user, etc.):')
    print(prompt)
    access1 = None
    access1 = input(str())


    print('Please enter users bulding number:')
    print(prompt)
    bldg = None
    bldg = int(input())

    cursor.execute('''INSERT INTO users(ID, NAME, ACCESS, BUILDING) VALUES (?,?,?,?)''',(id, name1, access1, bldg))
    db.commit()
    print('Insert complete')

elif a == '3': 
    
    print('thank you!')

            

