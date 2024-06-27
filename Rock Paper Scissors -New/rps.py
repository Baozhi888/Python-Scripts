import random

def get_user_choice():
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    user_choice = input("Enter your choice (rock, paper, scissors, lizard, spock): ").lower()
    while user_choice not in choices:
        user_choice = input("Invalid choice. Please enter rock, paper, scissors, lizard, or spock: ").lower()
    return user_choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    win_conditions = {
        "scissors": ["paper", "lizard"],
        "paper": ["rock", "spock"],
        "rock": ["lizard", "scissors"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
    }
    
    if user_choice == computer_choice:
        return "tie"
    elif computer_choice in win_conditions[user_choice]:
        return "user"
    else:
        return "computer"

def play_game():
    print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    winner = determine_winner(user_choice, computer_choice)
    
    if winner == "tie":
        print("It's a tie! Let's play again.")
        play_game()
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

if __name__ == "__main__":
    play_game()


