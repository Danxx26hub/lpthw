#!/usr/bin/env python3
# average hours alept in a week
# input hours slept per day

# import pdb ; pdb.set_trace()

days = ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']

hours = []
count = 0

while count < 6:
	print('Please tell me how many hours you slept on:')
	for day in days:
		print(day)
		value = float(input())
		hours.append(value)
		v = sum(value)
		count = count + 1
  
avg =  ((v) / 7)

print("you slept an average of", round(avg), 'hours')