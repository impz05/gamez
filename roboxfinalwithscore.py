import time
import random
import threading

print("Your score bank has 20 points in the start of the game") 

# Define the parts of digital numbers from 0-9
DIGIT_PARTS = {
    0: [" _ ", "| |", "|_|", "   "],
    1: ["   ", "  |", "  |", "   "],
    2: [" _ ", " _|", "|_ ", "   "],
    3: [" _ ", " _|", " _|", "   "],
    4: ["   ", "|_|", "  |", "   "],
    5: [" _ ", "|_ ", " _|", "   "],
    6: [" _ ", "|_ ", "|_|", "   "],
    7: [" _ ", "  |", "  |", "   "],
    8: [" _ ", "|_|", "|_|", "   "],
    9: [" _ ", "|_|", " _|", "   "],
}

user_guess = None  # Variable to store the user's guess

def input_with_timeout(prompt, timeout):
    global user_guess
    user_guess = None
    timer = threading.Timer(timeout, lambda: None)  # Timer to auto-continue if user doesn't respond
    timer.start()
    try:
        user_guess = input(prompt)
    except Exception as e:
        print(e)
    finally:
        timer.cancel()

def display_part(digit, part_idx):
    """Display the part of a given digit."""
    print(DIGIT_PARTS[digit][part_idx])

def digital_clock_guessing_game():
    global user_guess
    
    number_to_guess = random.randint(0, 9)#digital clock of a number between 0-9 is displayed
    score = 20  # Starting score
    print("Guess the number! A digital number part will be revealed every attempt you get wrong")

    
    for part_idx in range(4):
        
        display_part(number_to_guess, part_idx)

        
        input_with_timeout("Your guess (10 seconds): ", 10)

        
        if user_guess is not None:
            try:
                if int(user_guess) == number_to_guess:
                    print(f"Congratulations! You guessed it right! Your score: {score}")
                    return  
                else:
                    
                    score -= 5
            except ValueError:
                print("Invalid input. Please enter a number between 0-9.")
        else:
            print("Time's up! Moving to the next part...")
        
        
        print(f"Your score after this attempt: {score}")

        
        print("Revealing the next part in a moment...\n")

    print(f"Sorry, you're out of attempts. The correct number was {number_to_guess}.")
    print(f"Your final score is: {score}. Better luck next time!")


digital_clock_guessing_game()
