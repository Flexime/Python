# This line will automatically add a new line before the
# next print statement
print ("DSA content")

# This print() function ends with "**" as set in the end argument.
print ("DSA content", end= "**")

import time

count_seconds = 3
for i in reversed(range(count_seconds + 1)):
	if i > 0:
		print(i, end='>>>')
		time.sleep(1)
	else:
		print('Start')
  
  
count_seconds = 3
for i in reversed(range(count_seconds + 1)):
	if i > 0:
		print(i, end='>>>', flush = True)
		time.sleep(1)
	else:
		print('Start')

import io

# declare a dummy file
dummy_file = io.StringIO()

# add message to the dummy file
print('Hello Geeks!!', file=dummy_file)

# get the value from dummy file
dummy_file.getvalue()

# Python 3.x program showing
# how to print data on
# a screen

# One object is passed
print("GeeksForGeeks")

x = 5
# Two objects are passed
print("x =", x)

# code for disabling the softspace feature
print('G', 'F', 'G', sep ='')

# using end argument
print("Python", end = '@')
print("GeeksforGeeks")
