start = '''
You are the princess of Goldlake and soon to be the queen. You don't have any parents and are looking for the love fo your life.
'''

keepplaying = "yes"
print (start)
while keepplaying == "Yes" or keepplaying == "yes":
    userChoice = input("Who do you like better, Tyler or Brandon? Type 1 for Tyler and Type 2 for Brandon")
    if userChoice == "1":
        print ("Congrats, Tyler is your destined lover and he treats you well.")
        print ("The two of you become king and queen of Bluelake!")
        print("")
        keepplaying = "no"
    elif userChoice == "2":
        print ("Oh no! You have made the wrong choice")
        print ("Brandon from your enemy's kingdom and is a spy/assassin")
        print ("Sadly, he poison's your wine during dinner and you die")
        keepplaying = input("Would you like to try again? Type yes or no.")
    else:
        print("Please select a valid option 1 or 2")
        keepplaying = input("Would you like to try again? Type yes or no")
        if keepplaying == "no":
            quit()

keepplaying = "yes"
while keepplaying == "Yes" or keepplaying == "yes":
    userChoice = input("Does Tyler want two or four kids? Type 1 for two and 2 for four.")
    if userChoice == "1":
        print ("He loves you even more for agreeing with him and you live together forever.")
        print("You have a happily ever after.")
        print ("Thanks for playing!")
        print ("")
        quit()
    elif userChoice == "2":
        print ("He despises you and files for a divorce.")
        print ("Sadly, you die alone and without love")
        print ("You have failed")
    else: 
        quit()
