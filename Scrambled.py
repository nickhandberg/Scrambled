# Nicholas Handberg, Lab 4, 2/2/2021
# Topics: List, tuple
# Create a scrambled word game

def display_banner():                                                                   # Defines the display_banner() function and prints ASCII art
    print("""                                                                          
 __                               _      _            _ 
/ _\  ___  _ __  __ _  _ __ ___  | |__  | |  ___   __| |
\ \  / __|| '__|/ _` || '_ ` _ \ | '_ \ | | / _ \ / _` |
_\ \| (__ | |  | (_| || | | | | || |_) || ||  __/| (_| |
\__/ \___||_|   \__,_||_| |_| |_||_.__/ |_| \___| \__,_|
                                                        
""")

def load_words(filename):                                                               # Defines the load_words() function with parameter 'filename'

    scrambled_list = []                                                                 # Creates a empty list 'scrambled_list'
    answer_list = []                                                                    # Creates a empty list 'answer_list'
    with open(filename, 'r') as f:                                                      # Opens the file in read mode 
        for line in f:                                                                  # For loop to read line by line of the file
            (s,a) = line.strip().split(":")                                             # Splits the line by ":" and stores data before the split in 's' and the data after in 'a' 
            scrambled_list+=[s]                                                         # Adds the current 's' string to the 'scrambled_list'
            answer_list+=[a]                                                            # Adds the current 'a' string to the 'answer_list'
    return (scrambled_list, answer_list)                                                # Returns the 'scrambled_list' and 'answer_list'
            
            
def main():                                                                             # Defines the main() function
    
    display_banner()                                                                    # Calls the display_banner() function
    import random                                                                       # Imports the random module
    user_answer = 'temp'                                                                # Sets 'user_answer' to temp in order to start the while loop
    word_num = random.sample(range(0,18),18)                                            # Gets a random sample of 17 numbers and stores it in word_num
    
    (scrambled_list, answer_list) = load_words('Halloween.txt')                         # Calls the load_words() function with the argument 'Halloween.txt' and stores return in 'scrambled_list' and 'answer_list'
    
    for n in range(0,18):                                                               # For loop that will loop 17 times and stores the current loop number in 'n'
        
        hint = ' '                                                                      # Sets hint as a single space
        scram_temp = scrambled_list[word_num[n]]                                        # Gets a scrambled word using the random sample 'word_num' and current loop count 'n' and stores the respective element in 'scram_temp'
        ans_temp = answer_list[word_num[n]]                                             # Gets a answer word using the random sample 'word_num' and current loop count 'n' and stores the respective element in 'ans_temp'
        guesses = len(ans_temp)                                                         # Sets guesses to the length of the string from 'ans_temp'
        
        while user_answer != ans_temp:                                                  # While loop that will loop as long as the 'user_answer' does not equal 'ans_temp'
            
            print(f"\nScrambled word is:  {scram_temp}")                                # Prints the scrambled word to the user's screen
            print(f"You can guess {guesses} more time(s).")                             # Prints the amount of guesses the user has to the user's screen
            print("-------------------------------")
            user_answer = str(input("\nWhat is the word?\n\n>"))                        # Gets the user's input for 'user_answer'
            
            if user_answer != ans_temp:                                                 # If statement to check if the user got the wrong answer
                guesses -= 1                                                            # Subtracts 1 from 'guesses'
                
                if guesses == 0:                                                        # If statement to check if the user has run out of guesses
                    print("\nYou have run out of guesses.\nThanks for playing!")        # Prints that the user has run out of guesses and returns
                    return
                
                print("\nWrong answer. Try again!")                                     # Prints that the user got the wrong answer
                wrong_count = len(ans_temp) - guesses                                   # Counts how many times the user has gotten a wrong answer
                
                if wrong_count >= 2:                                                    # Checks if the user has gotten 2 or more wrong answers
                    hint = hint + ans_temp[wrong_count-2]                               # Gets the respective elements from 'ans_temp' and adds it to 'hint'
                    print(f'HINT: {hint} ')                                             # Prints the hint to the user
                    
        if n == 17:                                                                     # Checks if 'n' is equal to 17 (for loop has looped 17 times)
            print("\nYou have completed all the scrambled words.")                      # Prints that the user has completed all the scrambled words and breaks the for loop
            break
        
        another_game_temp = input("\nYou got it!\nAnother game? (Y/N):\n\n>")           # Gets the user's input if they would like another game
        another_game = another_game_temp.lower()                                        # uses .lower() to make the user's answer lowercase for ease of checking
        
        if another_game == 'n':                                                         # Checks if the user said no to another game and breaks the for loop
            break
        
     
    print("\nThanks for playing!")                                                      # Prints thanks for playing to the user's screen
        
        
main()                                                                                  # Calls the main() function

            
                        
