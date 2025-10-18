#!/usr/bin/python3
import random

def show_hands():
    # Once the player selects how much they want to bet
    # show the deck
    print("Dealer: ???")
    print(f"{hand_dealer}") # Show the dealer's hand

    print()

    print(f"Player: {sum(hand_player)}")
    print(f"{hand_player}") # Show the dealer's hand


# The game starts with 5000 cash
cash      = 5000
game_over = False
winner    = 0
WINNING_NUMBER = 21

# The game starts with the dealer and the player having two cards
hand_player = [random.randint(1, 13) for _ in range(0, 2)]
hand_dealer = [random.randint(1, 13) for _ in range(0, 2)]

# Choose amount to bet
bet = int(input(f"How much do you bet? (1 - {cash}, or QUIT) > "))

# After the player chooses his bet, show the hands
show_hands()

stand = False

while stand is not True:
    # Get input. Only double down if this is the first play
    player_input = input("(H)it, (S)stand, (D)double down > ")

    match(player_input.lower()):
        case 'h':
            hand_player.append(random.randint(1, 13))
            hand_dealer.append(random.randint(1, 13))
        case 's':
            stand = True;
        case 'd':
            # The player wants to double down:
            # We'll implement the logic for doubling down later
            pass
        case _:
            print('Unknown input sir!!')

    # After every play, print the current deck
    print()
    show_hands()

    # Check if there's any player who's exceeded the winning number
    player_sum = sum(hand_player)
    dealer_sum = sum(hand_dealer)

    if player_sum > WINNING_NUMBER or dealer_sum == WINNING_NUMBER:
        game_over = True
        winner    = 2
        break
    elif dealer_sum > WINNING_NUMBER or player_sum == WINNING_NUMBER:
        game_over = True
        winner    = 1
        break

    # TODO: Implement a situation where both the players exceed the
    # winning number

    # It's possible that both the players have exceeded the winning
    # number
    

# if the play was stopped let's determine who the winner is

if game_over is True:
    if (winner == 1):
        print("Player wins!!!! :)")
        cash += bet
    else:
        print("Player loses!!!! :)")
        cash -= bet
else:
    # This means the game was stopped    

    if (abs(WINNING_NUMBER - player_sum) < (WINNING_NUMBER - dealer_sum)):
        # The player has won
        print("Player wins!!!! :)")
        cash += bet
    elif (abs(WINNING_NUMBER - player_sum) == (WINNING_NUMBER - dealer_sum)):
        # This is a draw
        print("Game ends in a draw!!!")
        
        # Player earns nothing
    else :
        # The player has lost
        print("Player loses!!!! :)")
        cash -= bet


