import random
player_points = 0
computer_points = 0
while True:
    rock = "Rock"
    papper = "Papper"
    scissors = "Scissors"
    test = [rock, papper, scissors]
    player_move = input(f"Choose [r]ock, [p]apper or [s]cissors: ")
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = papper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit(f"Invalid input.Try again...")
    computer_random_move = random.choice(test)
    print(f"Computer chose {computer_random_move}")
    if (player_move == rock and computer_random_move == scissors) or \
        (player_move == scissors and computer_random_move == papper) or \
        (player_move == papper and computer_random_move == rock):
        print(f"You win!")
        player_points += 1
    elif player_move == computer_random_move:
        print(f"The game is a draw!")
    else:
        print(f"You lose!")
        computer_points += 1
    print(f"The current score is {player_points} : {computer_points}")
    play_again_option = input(f"Would you like to play another game? ")
    if play_again_option == "yes":
        continue
    elif play_again_option == "no":
        print(f"The final score is {player_points} : {computer_points}."
              f"Goodbye!")
        break

