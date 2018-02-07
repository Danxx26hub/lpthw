#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import sqlite3

prompt = '>'

db = sqlite3.connect('db1.db')

cursor = db.cursor()

cursor.execute('''SELECT ID, NAME, ACCESS FROM users''')

user1 = cursor.fetchone()

print('printing name of first user in database')
print(user1[1])

print('would you like to see all info?: y/n')
print(prompt)
a = input(str())

if a == 'y':

    all_rows = cursor.fetchall()

    for row in all_rows:
        print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))


else:
    print('thank you, would you like to add a user?')
    
    print(prompt)

    ans = input(str())



if ans  == 'y':
    print('Please enter users ID:')
    print(prompt)
    id  = input(int())

    print('Please enter users name:')
    print(prompt)
    name1 = input(str())


    print('Please enter users Access type (admin, user, etc.):')
    print(prompt)
    access1 = input(str())


    print('Please enter users bulding number:')
    print(prompt)
    bldg = input(int())

    cursor.execute('''INSERT INTO users(ID, NAME, ACCESS, BUILDING) VALUES (?,?,?,?)''',(id, name1, access1, bldg))
    db.commit()
    print('Insert complete')


            

