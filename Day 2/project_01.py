import random

def number_guessing():
    random_number = random.randint(1, 10)
    attempts = 0
    max_attempts = 5
    
    print("Welcome to the Number Guessing Game!")
    print(f"Guess a number between 1 and 10. You have {max_attempts} attempts.")
    
    while attempts < max_attempts:
        try:
            # Get user input and convert to integer
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: "))
            
            # Validate input range
            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10!")
                continue
                
            attempts += 1
            
            # Check guess against random number
            if guess == random_number:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                return True
            elif guess < random_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
                
        except ValueError:
            print("Invalid input! Please enter a whole number between 1 and 10.")
    
    print(f"Game over! The number was {random_number}.")
    return False

def main():
    while True:
        number_guessing()
        
        # Ask if player wants to play again
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

main()