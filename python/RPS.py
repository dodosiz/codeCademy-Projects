"""The programm is the classic game of rock paper scissors against the computer"""

from random import randint
from time import sleep

options = ["R", "P", "S"]

LOSE_MESSAGE = "You lost my friend, I am sorry."
WIN_MESSAGE = "Bravo my friend, you won!"

def decide_winner(user_choice, computer_choice):
	print "So you chose %s." % user_choice
	print "Computer selecting..."
	sleep(1)
	print "Computer chose %s." % computer_choice
	try:
		user_choice_index = options.index(user_choice)
	except ValueError:
		print "Hey man watch out your typing!"
		return
	computer_choice_index = options.index(computer_choice)
	if user_choice_index == computer_choice_index:
		print "It's a tie!"
	elif user_choice_index == 0 and computer_choice_index == 2:
		print WIN_MESSAGE
	elif user_choice_index == 1 and computer_choice_index == 0:
		print WIN_MESSAGE
	elif user_choice_index == 2 and computer_choice_index == 1:
		print WIN_MESSAGE
	else:
		print LOSE_MESSAGE
    
def play_RPS():
	print "Rock Paper Scissors!"
	user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors.\n>>").upper()
	computer_choice = options[randint(0,len(options)-1)]
	decide_winner(user_choice, computer_choice)
  
play_RPS()