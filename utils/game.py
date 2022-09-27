#Import required modules and libraries
import random


#Define hangman class
class Hangman():

    """
    Hangman game in Python, played in the terminal.
    """
    #List of possible words which combines a list of words chosen freely and a list of words that are mandatory
    possible_words_free_list = ['school','taxman','superhero','anticonstitutional','weird','behaviour','scratchy']
    possible_words_constrained_list = ['becode','learning','mathematics','sessions']
    possible_words = possible_words_free_list + possible_words_constrained_list

    def __init__(self):
        """
        Initialize variables used in the code.\n
        :word_to_find: the secret word you have to discover if you want to live.\n
        :correctly_guessed_letters: the list of letters correctly guessed.\n
        :wrongly_guessed_letters: the list of letters wrongly guessed.\n
        :already_guessed_letters: the contatenation of the lists of correctly and wrongly guessed letters.\n
        :lives: the player's number of lives.\n
        :turn_count: the number of turns already played.\n
        :error_count: the number of incorrect guesses already made.\n
        :success_count: the number of correct letters already found.\n
        """

        #Randomly select a word from the possible_words list.
        self.word_to_find = random.choice(Hangman.possible_words)
        #Initiate lists for correctly, wrongly and already guessed letters.
        self.correctly_guessed_letters = list()
        self.wrongly_guessed_letters = list()
        self.already_guessed_letters = list()
        #Player's number of lives.
        self.lives = 5
        #Initiate variable for counting the number of turns played.
        self.turn_count = 0
        #Initiate variable for counting the number of incorrectly guessed letters.
        self.error_count = 0
        #Initiate variable for counting the number of correctly guessed letters.
        self.success_count = 0


    def play(self):
        """
        The games' sequence of play.\n
        The player is asked to guess a letter.\n
        The input is checked for validity.\n
        The guessed letter is checked against the letters in the secret word.\n
        Results are printed.\n
        """

        #Ask the player to guess a letter.
        self.guessed_letter = input("Please guess a letter: ")

        #Check for the validity of the input, indicate if the letter was already proposed and then check if the letter belongs to the secret word or not.
        if len(self.guessed_letter) !=1:
            print("Please enter 1 letter only")
        elif self.guessed_letter.isalpha() == False:
            print("Please enter 1 LETTER")
        elif self.guessed_letter in self.already_guessed_letters:
            print("You already guessed this letter!")
        else:
            if self.guessed_letter in self.word_to_find:
                self.correctly_guessed_letters.append(self.guessed_letter)
                print("Bravo! Good guess!")
            else:
                self.wrongly_guessed_letters.append(self.guessed_letter)
                print("Sorry, wrong guess!")
                self.error_count += 1
                self.lives -= 1
        self.turn_count +=1

        self.already_guessed_letters = self.correctly_guessed_letters + self.wrongly_guessed_letters

        #Display correctly guessed letters and underscore characters for remaining letters of the secret word.
        self.success_count = 0
        for letter in self.word_to_find:
            if letter in self.correctly_guessed_letters:
                print(f"{letter}", end=" ")
                self.success_count += 1
            else:
                print("_", end = " ")

        print("")
        print("well_guessed_letters: ", self.correctly_guessed_letters)
        print("bad_guessed_letters: ", self.wrongly_guessed_letters)
        print("Error_count: ", self.error_count)
        print("Success_count: ", self.success_count)
        print("Remaining_lives: ", self.lives)
        print("Turn_count :", self.turn_count)

        #Condition to call the well_played() function.
        if self.success_count == len(self.word_to_find):
            self.well_played()


    def game_over(self):
        """
        Function that is called when the player is unsuccessful and has lost all remaining lives.\n
        Prints "game over".\n
        Exits the game.\n
        """
        print("game over")
        exit()

    def well_played(self):
        """
        Function that is called when the player has successfully found all the letters of the secret word.\n
        Prints the secret word, number of turns played and number of errors made.\n
        Exits the game.\n 
        """
        print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!")
        print("Bravo")
        exit()

    def start_game(self):
        """
        Function that is called at the start of the game.\n
        Starts by displaying underscore characters for the letters in the secret word.\n
        Calls the play() function if the player has still some remaining lives and the game_over() function otherwise.\n
        """
        for letter in self.word_to_find:
            print("_", end=" ")

        while self.lives > 0:
            self.play()
        else:
            self.game_over()
