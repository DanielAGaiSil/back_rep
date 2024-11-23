#concatenating strings
#suppose we want to print a string that says "please do ____ "
#this ="that" #whatever you will do
#print(f"please do {this}")

adj = input("Type an adjective: ")
verb1= input("Type a verb: ")
verb2= input("Type another verb: ")
noun = input("Type a noun: ")

madlib = f"Doing this is so {adj}! It's really easy when you {verb1} \
Since, you know, {noun} is helping me out. I really have to {verb2}."

print(madlib)