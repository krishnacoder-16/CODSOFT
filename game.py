import random
print("Rock","Scissors","Paper","Game")
def game():
    user=input("enter your choice(rock,paper,scissors):").strip().lower()
    actions=["rock","paper","scissors"]
    computer_action=random.choice(actions)
    print(f"\nYou chose {user}, computer chose {computer_action}.\n")
    if user == computer_action:
        print(f"Both players selected {user}. It's a tie!")
    elif user == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
while True:
     game()
     play_again = input("Play again? (yes/no): ")
     if play_again.lower() == "no":
         break