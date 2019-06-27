# the one with a bit of problems 
secret_word = "disneyland"
guess_word = []
length_word = len(secret_word)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []

def change():

    for character in secret_word: # printing blanks for each letter in secret word
        guess_word.append("-")
def guessing():
    guess_taken = 1

    while guess_taken < 10:


        guess = input("Pick a letter\n").lower()

        if not guess in alphabet: #checking input
            print("Enter a letter from a-z alphabet")
        elif guess in letter_storage: #checking if letter has been already used
            print("You have already guessed that letter!")
        else: 

            letter_storage.append(guess)
            if guess in secret_word:
                print("You guessed correctly!")
                for x in range(0, length_word): #This Part I just don't get it
                    if secret_word[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)

                if not '-' in guess_word:
                    print("You won!")
                    break
            else:
                print("The letter is not in the word. Try Again!")
                guess_taken += 1
                if guess_taken == 10:
                    print(" Sorry Mate, You lost :<! The secret word was",         secretWord)


change()
guessing()

print("Game Over!")