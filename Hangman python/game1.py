import random

class Hangman:
    
    def display_welcome(self):
        # Display the welcome message and category options
        print("\t\t\t\t\t\tWelcome to Hangman")
        print("+---------------------------------------------------------------------------------------------------------------------+")
        print("+---------------------------------Select one of the categories from the following.------------------------------------+")
        print("\t\t !! Note: The word that you will get to solve depends on which category you choose !!")
        print("\t 1. States of Gujarat")
        print("\t 2. Fruits")
        print("\t 3. Countries of Asia")
        print("\t 4. Someone from our class")

    def select_category(self):
        while True:
            # Get user input for the selected category
            category_input = input("\tEnter your selected category: ")

            # Check if the input is a valid digit
            if not category_input.isdigit():
                print("\t!! Please enter a valid digit (1-4) !!")
                continue

            category = int(category_input)

            # Check if the category is within the valid range
            if 0 < category < 5:
                # Open the corresponding text file based on the selected category
                if category == 1:
                    selected_file = open("States_of_Gujarat.txt")
                elif category == 2:
                    selected_file = open("Fruits.txt")
                elif category == 3:
                    selected_file = open("Country.txt")
                elif category == 4:
                    selected_file = open("class_names.txt")
                else:
                    print("\t !! Invalid choice !!")
                    continue
                break  # Exit the loop if a valid category is selected
            else:
                print("\t !! Invalid choice !!")

        return selected_file

    def play_game(self):
        while True:
            # Initialize life for a new game
            life = 3
            # Display the welcome message and get the selected category
            self.display_welcome()
            f = self.select_category()
            l = f.readlines()
            f.close()
            result = []

            # Choose a random word from the selected category
            word = random.choice(l).rstrip().lower()
            
            # Get player's name and ensure it is not empty
            name = input("\tEnter your name: ")
            while not name:
                print("\t!! Name cannot be empty !!")
                name = input("\tEnter your name: ")
            
            # Set the visible letter (first letter of the word)
            visible_letters = word[0]

            # Initialize the result with underscores for unrevealed letters
            for i in word:
                if i == visible_letters:
                    result.append(i + " ")
                else:
                    result.append("_ ")

            while True:
                print("+---------------------------------------------------------------------------------------------------------------------+")
                out = []

                if life == 0:
                    # Display Game Over message if player runs out of lives
                    print("+---------------------------------------------------------------------------------------------------------------------+")
                    self.print_colored("\n\t\t\t\t\t\tGame Over! You lost.", 'red')
                    print("\t\t\t\t\t\tThe word is:", word)
                    print("\n+---------------------------------------------------------------------------------------------------------------------+")
                    break

                print("\n\tPlayer:", name, "\t\tLife remaining:", "❤ " * life)
                print("\tWord is", "".join(result))

                # Get the player's guess and ensure it is a single lowercase letter
                guess = input("\tEnter your guess (single lowercase letter) : ")
                while not (guess.isalpha() and len(guess) == 1):
                    print("\t!! Please enter a single lowercase letter !!")
                    guess = input("\tEnter your guess (single lowercase letter) : ")

                if guess not in word:
                    # Decrement life if the guessed letter is not in the word
                    life -= 1
                else:
                    # Update the result with the correctly guessed letter
                    for i in word:
                        if i == guess or i == visible_letters:
                            out.append(i + " ")
                        else:
                            out.append("_ ")

                    for i in range(len(word)):
                        if result[i] == "_ ":
                            result[i] = out[i]
                    
                    # Check if all letters are revealed, and display a victory message
                    if result.count("_ ") == 0:
                        print("+---------------------------------------------------------------------------------------------------------------------+")
                        print("\n\t\t\t\t\tCongratulations! You Won The Game!\n\t\t\t\t\tWord is:", word)
                        print("\n+---------------------------------------------------------------------------------------------------------------------+")
                        break

            # Ask if the player wants to play again
            replay = input("\tDo you want to play again? (yes/no): ")
            if replay.lower() not in ['yes', 'y']:
                # If the player chooses not to play again, display a farewell message and exit the loop
                print("\n\tThank you for playing Hangman! Goodbye.")
                break
    def print_colored(self, text, color):
        colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'purple': '\033[95m',
            'cyan': '\033[96m',
            'bold': '\033[1m',
            'underline': '\033[4m',
            'reset': '\033[0m'
        }
        print(colors[color] + text + colors['reset'])

   
# Create an instance of the Hangman class and start the game
hangman_game = Hangman()
hangman_game.play_game()