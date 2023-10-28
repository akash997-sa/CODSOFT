import random
user_score = 0
computer_score = 0
def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "rock") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "You lose!"
def display_scores():
    print(f"Scores - You: {user_score}, Computer: {computer_score}")
while True:
    user_choice = input("\nchoose rock, paper, or scissors").lower()
    if user_choice not in ["rock", "paper", "scissors."]:
        print("Invalid choice.Please enter rock, paper, or scissors")
        continue
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"\nYou chose {user_choice}.I chose {computer_choice}.")
    result = determine_winner(user_choice, computer_choice)
    print(result)
    display_scores()
    play_again = input("\nDo you want to play again?(yes/no):").lower()
    if play_again!= "yes":
        break
    print("Thanks for playing")




