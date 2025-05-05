import random


# game function
def game():
    print(f"Welcome to the Rock Paper Scissors game\n")
    print("""
    Rock
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    
    Paper
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    
    Scissors
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    
    """)

    while True:
        choice = None
        try:
            choice = int(input("\nEnter:\n1 for Rock\n2 for Paper\n3 for Scissors\n"))
            if choice not in [1, 2, 3]:
                print("Please enter 1, 2, or 3")
                continue
        except ValueError:
            print("Invalid input")

        computer = random.randint(1, 3)
        choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

        print(f"You chose {choices[choice]}\nComputer chose {choices[computer]}\n")

        if choice == computer:
            print("Tie")
        elif (choice == 1 and computer == 3) or \
                (choice == 2 and computer == 1) or \
                (choice == 3 and computer == 2):
            print("You won")
        else:
            print("You lose")

        # play again logic
        replay = str(input("Play Again? y to play again, n to quit"))
        if replay.lower() != 'y':
            break


game()
