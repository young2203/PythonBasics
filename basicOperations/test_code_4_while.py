#!/usr/bin/python
# Filename: while.py
number = 23
running = True
while running:
	guess = int(raw_input('Enter an integer : '))
	#If Block to compare the input with preset number
	if guess == number:
		print 'Congratulations, you guessed it.'
		running = False # this causes the while loop to stop
	elif guess < number:
		print 'No, it is a little higher than that'
	else:
		print 'No, it is a little lower than that'
	#End of If Block (comparing)
else:
	print 'The while loop is over.'
# Do anything else you want to do here
print 'Done'

print 'New While Loop'
number = 23
running = True
while running:
	guess = int(raw_input('Enter an integer : '))
	#If Block to compare the input with preset number
	if guess == number:
		print 'Congratulations, you guessed it.'
		running = False # this causes the while loop to stop
	elif guess < number:
		print 'No, it is a little higher than that'
	else:
		print 'No, it is a little lower than that'
	#End of If Block (comparing)

# Do anything else you want to do here
print 'Done'