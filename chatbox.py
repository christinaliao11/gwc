# --- Define your functions below! ---
start = 'Hello, I am ... your personal therapist. I am here to listen to your problems. '

cont = "yes"
print (start)

while cont == "Yes" or cont == "yes":
    userChoice = input("Are you feeling not okay or okay? Type 1 for not okay and type 2 for okay.")
    if userChoice == "1":
        print ("I'm sorry you feel that way .")
        print ("Would you like to hear a joke? ")
        userChoice = input("Type 1 for yes and 2 for leave me alone.")
        if userChoice =="1":
            print("Why do cows have hooves instead of feet? ")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("They lactose. AHAHA. I hope that made you laugh.")
            userChoice = input("TO make you feel better here are some puppies! Do you want them? Type 1 for yes and 2 for no.")
            if userChoice =="1":
                print("They have been shipped and are on their way. I hope you enjoy!")
            if userChoice =="2":
                print("I am sorry the puppies are not a match for you. I would still like to help you.")
            
        if userChoice =="2":
            print("I'm sorry I am no help, I will direct you to a human therapist.")
            userChoice == input("Type bye to exit.")
            if userChoice =="bye":
                print("Bye!")
            quit()

        
        cont == "no"
        quit()
    elif userChoice  == "2":
        userChoice == input("Cool! Tell me something good that happened to you today? Type in your answer. " )
        print()
        print("That is so cool. Amazing. Let me tell you a joke!")
        print("")
        print("")
        print("")
        print("I tell people I’m on a low-carb diet. But in reality, I just eat pasta while lying on the floor.")
        print("**reserved laughing in the corner of the room**")
        print("")
        print("Thanks for listening to my corny joke. I hope you have an amazing rest of your day! Bye!")

        cont == "no"
        quit()
    else:
        print ("Can I direct you to a human therapist?")
        cont = input("Would you like a human therpist? Type yes or no")
        if cont == "yes":
            print("I will direct you to them! Bye!")
            quit()
        if cont == "no":
            userChoice == input("Would you like to start over? Type yes or no")
            if cont == "yes":
                    print(start)
            if cont == "no":
                print("Bye!")
                quit()


# --- Put your main program below! ---
def main():
  while True:
    answer = input("(How are you?) ")
    print("That's cool!")


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()