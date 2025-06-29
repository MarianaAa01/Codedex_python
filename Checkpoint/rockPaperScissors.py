
#Rules:
#   Scissors cut Paper.
#   Paper covers Rock.
#   Rock crushes Lizard.
#   Lizard poisons Spock.
#   Spock smashes Scissors.
#   Scissors beat Lizard.
#   Lizard eats Paper.
#   Paper disproves Spock.
#   Spock vaporizes Rock.
#   Rock breaks Scissors.


# In this game:
#   1 is for '✊' (Rock).
#   2 is for '✋' (Paper).
#   3 is for '✌️' (Scissors).
#   4 is for '🖖' (Spock).
#   5 is for '🦎' (Lizard).


import random

print("=================== \n Rock Paper Scissors \n =================== \n\n")
print("1) ✊ \n2) ✋ \n3) ✌️ \n4) 🦎 \n5) 🖖 \n")
hand_signs = ["✊", "✋", "✌️", "🦎", "🖖"]

player = int(input("Choose a number between 1 and 5: "))
computer = random.randint(1, 5)

print("You chose: " + hand_signs[player-1])
print("CPU chose: " + hand_signs[computer-1])

if ((player == 1 and computer == 3) or
    (player == 3 and computer == 2) or
    (player == 2 and computer == 1) or
    (player == 1 and computer == 4) or
    (player == 4 and computer == 5) or
    (player == 5 and computer == 3) or
    (player == 3 and computer == 4) or
    (player == 4 and computer == 2) or
    (player == 2 and computer == 5) or
    (player == 5 and computer == 1)):
    print("The player won!\n")
elif (player == computer):
    print("It's a tie! Try again.\n")
else:
    print("CPU won!\n")