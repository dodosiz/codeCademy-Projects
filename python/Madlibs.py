"""This programm prints to the user a story with
blank spaces and asks him to fill them, it prints
finally the whole story out."""
print "Mad Libs started sucessfully."
user_name = raw_input("What's your name?\n>>")
# asking for 3 adjectives to create the story
print "You will now be aked to input 3 adjectives."
adjective1 = raw_input("Adjective 1 is:\n>>")
adjective2 = raw_input("Adjective 2 is:\n>>")
adjective3 = raw_input("Adjective 3 is:\n>>")
# asking for 3 verbs also
print "You will now be asked to input 3 verbs."
verb1 = raw_input("Verb 1 is:\n>>")
verb2 = raw_input("Verb 2 is:\n>>")
verb3 = raw_input("Verb 3 is:\n>>")
# nouns are also to be asked
print "You will be asked now for 3 nouns."
noun1 = raw_input("Noun 1 is:\n>>")
noun2 = raw_input("Noun 2 is:\n>>")
noun3 = raw_input("Noun 3 is:\n>>")
noun4 = raw_input("Noun 4 is:\n>>")
# asking for some more stuff we need
animal = raw_input("Tell me an animal you think:\n>>")
food = raw_input("A food?\n>>")
fruit = raw_input("Oh, and a fruit would be great:\n>>")
number = raw_input("A number between zero and infinity?\n>>")
superhero = raw_input("A great superhero you mirin:\n>>")
country = raw_input("A country:\n>>")
dessert = raw_input("Can you think of a dessert too?\n>>")
year = raw_input("Finally, a year:\n>>")
#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rythym of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world." % (adjective1, user_name, verb1, adjective2, noun1, noun2, animal, food, verb2, noun3, fruit, adjective3, user_name, verb3, number, user_name, superhero, superhero, user_name, country, user_name, dessert, user_name, year, noun4)
print " --   -- " 
print "  o   o  "
print "    |    "
print "   ___   "
print "    U    "
print "\n!!! READ YOUR STORY NOW !!!\n\n"
print STORY
print "\nWhat a mess hahahahaha :)\n"