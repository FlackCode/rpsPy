import random
import time
print("Welcome to my Rock, Paper, Scissors game!")
movesArray = ["rock", "paper", "scissors"]
while True:
    userInput = input("Enter your move(rock, paper or scissors): ").lower()
    if userInput not in movesArray:
        print("Invalid move selected! Please select a correct move!!")
        continue
    computerInput = random.choice(movesArray)
    print("You chose: " + userInput)
    print("Computer chose: " + computerInput)
    print("Selecting winner...")
    time.sleep(2)
    if userInput == computerInput:
        print("Game ended in a tie!")
    elif (userInput == 'rock' and computerInput == 'scissors') or \
        (userInput == 'paper' and computerInput == 'rock') or \
        (userInput == 'scissors' and computerInput == 'paper'):
        print("User won!")
    else:
        print("Computer won!")
    playAgain = input("Would you like to play again?(yes/no): ").lower()
    if playAgain != "yes":
        print("Thank you for playing!")
        break