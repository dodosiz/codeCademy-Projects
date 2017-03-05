"""This programm is a dice game against the computer, the player must guess a number greater than the result to win."""

from random import randint
from time import sleep

def get_user_guess():
	user_guess = int(raw_input("What number do you choose\n>>"))
	return user_guess
	
def roll_dice(number_of_sides):
	first_roll = randint(1, number_of_sides)
	second_roll = randint(1, number_of_sides)
	max_val = number_of_sides * 2
	print "The maximum possible value is " + str(max_val)
	sleep(1)
	user_guess = get_user_guess()
	if user_guess > max_val:
		print "InputError: input larger than the max value."
		return
	else:
		print "Rolling..."
		sleep(2)
		print "First roll is %d" % first_roll
		sleep(1)
		print "Second roll is %d" % second_roll
		sleep(1)
		total_roll = first_roll + second_roll
		print "Result..."
		sleep(1)
		if user_guess >= total_roll:
			print "Congrats you just won!"
			return
		else:
			print "I am sorry you lost, better luck next time!"
			return
			
roll_dice(6)