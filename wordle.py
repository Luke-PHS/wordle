import random

possible_words = ["great", "thumb", "seven", "three", "kaleb", "salad"] 


word = random.choice(possible_words)


default = '\033[0m'
green = '\033[92m'
yellow = '\033[33m'



def generate_hint(user_guess):
    color - default
    hint = " "
    for i in range(5):
        if (user_guess[1] == word[i]):
            color = green
        elif (user_guess[1] in word):
            color = yellow
        else:
            color = default 
        
        hint = hint + color + user_guess[i] + default

        return hint
    
    return user_guess 



def game_loop():
    # looping 6 times
    guess = " "
    for i in range(6):
        guess = input("what is your guess: ")
        if (guess == word):
            print("congratulations!!!")
            break

game_loop()



