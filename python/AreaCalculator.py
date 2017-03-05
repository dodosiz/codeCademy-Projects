"""The programm asks the user to select either a circle or a triagle and then depending on the shape it calculates and displays the area."""

from math import pi
from time import sleep
from datetime import datetime
# info about current date and time
now = datetime.now()
# greeting the user
print "Welcome to Area Calculator!"
print "%s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)
sleep(1) # sleep for 1 sec
# Important piece of advice
hint = "Don't forget to include the correct unit."
# What will the shape be?
option = raw_input("Enter C for Circle or T for Triangle: ").upper()
# Calculate the area
if option == 'C':
	radius = float(raw_input("Radius of circle: "))
	area = pi * (radius ** 2)
	print "The pie is baking..."
	sleep(1)
	print "Area of circle: %.2f\n%s" % (area, hint)
elif option == 'T':
	base = float(raw_input("Base of triangle: "))
	height = float(raw_input("Height of triangle: "))
	area = (base * height) / 2
	print "Uni Bi Tri..."
	sleep(1)
	print "Area of triangle: %.2f\n%s" % (area, hint)
else:
	print "You didn't enter the correct input."
	print "The programm will exit."