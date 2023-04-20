import random
import time
import os


# Defining a function called clear to clear each words
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# Defining a class called JumbledWordGame
class JumbledWordGame:
    def __init__(self):
        self.wordlist = ['python', 'keyboard', 'processor', 'programming', 'hardware', 'internet', 'microsoft', 'microprocessor', 'registers', 'backup']
        self.score = 0
        self.lives = 3

# Defining a method called play to retrieve each word and then removes it from list

    def play(self):
        word = self.wordlist[0]
        self.wordlist.pop(0)
        jumbled = self.jumble(word)
        print(f"Jumbled word: {jumbled}")

# Start the timer

        start_time = time.time()
        while True:
            guess = input("Guess the word: ")
            if len(guess) != len(word):
                print("Your guess is invalid")
            elif not guess.isalpha():
                print("Your guess must be only letters")
            else:
                break

# Stop the timer

        end_time = time.time()
        clear()

        if guess.lower() == word.lower():
            print("Correct!")
            self.score += 1
        else:
            print(f"Incorrect. The word was {word}.")
            self.lives -= 1
            self.wordlist.append(word)

        print(f"Time taken: {end_time - start_time:.2f} seconds")
        print(f"Score: {self.score}  Lives: {self.lives}\n")

# Defining a method called jumble to jumble a word

    def jumble(self, word):
        jumbled = list(word)
        while True:
            random.shuffle(jumbled)
            if ''.join(jumbled) != word:
                break
        return ''.join(jumbled)


# Defining a function called show_instructions to display instructions for game


def show_instructions():
    print("Welcome to the jumbled word game!")
    print("Unscramble the jumbled word and type in your guess.")
    print("You have three lives. Each incorrect guess will cost you a life.")
    print("If you lose all your lives, the game is over.")
    print("Your score will increase by one for each correct guess.")
    print("Good luck!\n")


# Defining a function called play_game to play the game

def play_game():
    game = JumbledWordGame()
    random.shuffle(game.wordlist)
    while game.lives > 0 and len(game.wordlist) > 0:
        game.play()
        if game.lives == 0:
            clear()
            print("Game over!")
            break
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != 'y':
        clear()
        print(f"Final score: {game.score}")
    else:
        clear()
        print("Starting a new game...")
        game.score = 0
        game.lives = 3
        main()

# Defining the main function


def main():
    show_instructions()
    play_game()


if __name__ == '__main__':
    clear()
    main()
