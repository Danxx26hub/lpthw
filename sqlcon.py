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
    print('thank you')

