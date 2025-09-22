import random #Importing the random module to generate computer choices

def main():
    choices = ['rock', 'paper', 'scissors']
    user_score = 0 #initializing choices and scores
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors! \n please enter your choice (rock, paper, scissors) or 'quit' to exit.")
    #welcome massage

    while True: #main game loop

        user_choice = input("Your choice: ").lower().strip() #taking input from user

        if user_choice == 'quit':
            print(f"Thanks for playing! Final scores - You: {user_score}, Computer: {computer_score}")
            break
        if user_choice not in choices: #validating user input
            print("Looks like your enter have a problem,try again")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}") #generating computer choice

        if user_choice == computer_choice: #determining the winner
            print("Tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
                (user_choice == 'paper' and computer_choice == 'rock') or \
                (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win this round!")
            user_score += 1
            print(f"Scores - You: {user_score}, Computer: {computer_score} \nLets play again?")
        else:
            print("Computer wins this round!")
            computer_score += 1
            print(f"Scores - You: {user_score}, Computer: {computer_score} \nLets play again?")

main() #calling the main function to start the game