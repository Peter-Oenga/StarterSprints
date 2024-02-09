import random

def roll():
    min_value = 1
    max_value = 6
    roll_dice = random.randint(min_value, max_value)
    return roll_dice

while True:
    players = input("Enter the number of players (Between 2 -4): ")

    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 and 4")
    else:
        print("Invalid input!")
max_score = 50

player_score = [0 for _ in range(players)]

while max(player_score) < max_score:
    for player_index in range(players):
        current_score = 0
        print()
        print("Player number ", player_index + 1, "it is your turn to play")
        print("Your total score is ", player_score[player_index])
        print()

        while True:
            should_roll = input("Do you want to roll?, type y ")

            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                current_score += 0
                print("You rolled a 1, Turn is up!")
                break
            else:
                current_score += value
                print("You rolled a", value)
                print("Your total score is", current_score)

        player_score[player_index] += current_score
        print("Your total score is", player_score[player_index])

winning_index = player_score.index(max(player_score))
print("Congratulations player number", winning_index + 1, "You won!! with a total score of",
      player_score[winning_index])



