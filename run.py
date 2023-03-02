import random
class JumbledWordGame:
    def __init__(self, wordlist):
        self.wordlist = wordlist
        self.score = 0
        self.lives = 3

    def play(self):
        word = random.choice(self.wordlist)
        jumbled = self.jumble(word)
        print(f"Jumbled word: {jumbled}")
        guess = input("Guess the word: ")
        if guess == word:
            print("Correct!")
            self.score += 1
        else:
            print(f"Incorrect. The word was {word}.")
            self.lives -= 1
        print(f"Score: {self.score}  Lives: {self.lives}\n")
        

    def jumble(self, word):
        

def load_wordlist(filename):




def show_instructions():




def play_game(wordlist):





def main():


