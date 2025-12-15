Sweet_points = 0
Salty_points = 0
Spicy_points = 0

print ("Welcome to my personality quiz!")
input("")


answer1 = input("What kind of movie do you gravitate towards when you need comfort? A, wholesome and feel good, B action or mystery, or C Thriller or intense dramas ")
if answer1 == "A" or answer1 == "a":
    Sweet_points += 1
elif answer1 == "B" or answer1 == "b":
    Salty_points += 1
elif answer1 == "C" or answer1 == "c":
    Spicy_points += 1
input("")

answer2 = input ("How do you deal with conflict? A, staying gentle and calm, B staying grounded and practical, or C, Confront it head on? ")
if answer2 == "A" or answer2 == "a":
    Sweet_points += 1
elif answer2 == "B" or answer2 == "b":
    Salty_points += 1
elif answer2 == "C" or answer2 == "c":
    Spicy_points += 1
input("")

answer3 = input ("Whats your go-to vibe in a group setting? A, Friendly and warm, B, laid back and sarcastic, or C, chaotic and bold? ")
if answer3 == "A" or answer3 == "a":
    Sweet_points += 1
elif answer3 == "B" or answer3 == "b":
    Salty_points += 1
elif answer3 == "C" or answer3 == "c":
    Spicy_points += 1
input("")

answer4 = input ("What kind of compliment do you appreciate most? A, Your so kind, B, Your so reliable, or C Your so fearless " )
if answer4 == "A" or answer4 == "a":
    Sweet_points += 1
elif answer4 == "B" or answer4 == "b":
    Salty_points += 1
elif answer4 == "C" or answer4 == "c":
    Spicy_points += 1
input("")

answer5 = input ("What type of surprise do you enjoy? A, a cute note or treat, B, a practical gift or favor, or C, an unexpected adventure " )
if answer5 == "A" or answer5 == "a":
    Sweet_points += 1
elif answer5 == "B" or answer5 == "b":
    Salty_points += 1
elif answer5 == "C" or answer5 == "c":
    Spicy_points += 1
input("")

if Sweet_points > Salty_points and Sweet_points > Spicy_points:
    print("You have such a Sweet personality")
elif Salty_points > Spicy_points and Salty_points > Sweet_points:
    print("You have a Salty personality!")
elif Spicy_points > Salty_points and Spicy_points > Sweet_points:
    print("You have a Spicy personality!")
else:
    print("You have a mix of multiple personality traits!")