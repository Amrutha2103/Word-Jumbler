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
        jumbled = list(word)
        random.shuffle(jumbled)
        return ''.join(jumbled)
        
def load_wordlist(filename):
     with open(filename, 'r') as f:
        wordlist = [word.strip() for word in f.readlines()]
    return wordlist

def show_instructions():
    print("Welcome to the jumbled word game!")
    print("Unscramble the jumbled word and type in your guess.")
    print("You have three lives. Each incorrect guess will cost you a life.")
    print("If you lose all your lives, the game is over.")
    print("Your score will increase by one for each correct guess.")
    print("Good luck!\n")

def play_game(wordlist):





def main():


