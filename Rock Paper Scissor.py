import random

def get_user_choice():
    return input("Enter your choice: rock/paper/scissor\n").lower()

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Draw"
    elif (user_choice == 'rock' and computer_choice == 'scissor') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissor' and computer_choice == 'paper'):
        return f"{user_choice.capitalize()} beats {computer_choice}. You win!"
    else:
        return f"{computer_choice.capitalize()} beats {user_choice}. You lose!"

user_score = 0
computer_score = 0

print("Welcome to Rock, Paper, Scissors game")

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    if 'win' in result:
        user_score += 1
    elif 'lose' in result:
        computer_score += 1

    print(f"Score - You: {user_score}, Computer: {computer_score}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
