import random

SCORE_FILE = "scores.txt"

# Function to get user's choice
def get_user_choice():
    valid_choices = ['rock', 'paper', 'scissors']
    while True:
        choice = input("Enter your choice (rock/paper/scissors) or 'q' to quit: ").lower()
        if choice == 'q':
            return None
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice. Please try again.")

# Function to get computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "user"
    else:
        return "computer"

# Function to save scores to a file
def save_scores(scores):
    with open(SCORE_FILE, 'w') as file:
        for key, value in scores.items():
            file.write(f"{key}:{value}\n")

# Function to load scores from a file
def load_scores():
    scores = {}
    try:
        with open(SCORE_FILE, 'r') as file:
            for line in file:
                key, value = line.strip().split(":")
                scores[key] = int(value)
    except FileNotFoundError:
        pass
    return scores

# Main game function
def play_game():
    # Load scores from the file
    scores = load_scores()
    user_score = scores.get("user", 0)
    computer_score = scores.get("computer", 0)
    draws = scores.get("draws", 0)

    print("Welcome to Rock, Paper, Scissors!")

    while True:
        # Get user's choice
        user_choice = get_user_choice()
        if user_choice is None:
            break

        # Get computer's choice
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}\n")

        # Determine the winner
        winner = determine_winner(user_choice, computer_choice)

        if winner == "draw":
            print("It's a draw!")
            draws += 1
        elif winner == "user":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        # Update scores dictionary
        scores = {
            "user": user_score,
            "computer": computer_score,
            "draws": draws
        }

        # Save scores to the file
        save_scores(scores)

        print(f"\nScore - You: {user_score} | Computer: {computer_score} | Draws: {draws}\n")

    print("\nThanks for playing!")

# Start the game
play_game()
