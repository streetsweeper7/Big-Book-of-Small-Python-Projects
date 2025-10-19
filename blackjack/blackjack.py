#!/usr/bin/python3
import random
import sys

# The game starts with 5000 cash
game_over = False
winner    = 0
WINNING_NUMBER = 21

# Create a card class
class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
            
    def suit_symbol(self):
        return chr(0x2660 + self.suit)

    def value(self):
        return min(self.rank, 10)

    def rank_symbol(self):
        symbol = ''
        if self.rank == 1:
            symbol = 'A'
        elif self.rank == 11:
            symbol = 'J'
        elif self.rank == 12:
            symbol = 'Q'
        elif self.rank == 13:
            symbol = 'K'
        else:
            symbol = self.rank

        return symbol

    def top_border(self):
        if self.rank == 10:
            extra = '_'
        else:
            extra = ''
        return ' ___' + extra + ' '

    def top_line(self):
        return f'|{self.rank_symbol()}  |'

    def middle_line(self):
        if self.rank == 10:
            space = ' '
        else:
            space = ''
        return '| ' + self.suit_symbol() + space + ' |' 

    def bottom_line(self):
        return '|__' + f'{self.rank_symbol()}|'
         

# Player class
class Player():

    def __init__(self, type):
        self.cash = 5000    # The player's initial cash
        self.type = type
        self.hand = [Card(random.randint(1, 13), random.randint(0, 7))
                     for _ in range(0, 2)]

    def show_hand(self, hide_top_card=False):
        print()
        
        if hide_top_card is True:
            print(f"{self.type}: ###")
        else:
            print(f"{self.type}: {self.get_score()}")

        top_border  = ''
        top_line    = ''
        middle_line = ''
        bottom_line = ''

        for i, card in enumerate(self.hand):
            if i == (len(self.hand) - 1) and hide_top_card is True:
                # Hide the top card 
                top_border += " " * 2 + card.top_border()
                top_line   += " " * 2 + "|## |"
                middle_line   += " " * 2 + "|###|"
                bottom_line   += " " * 2 + "|_##|"
            else:
                top_border  += " " * 2 + card.top_border()
                top_line    += " " * 2 + card.top_line()
                middle_line += " " * 2 + card.middle_line()
                bottom_line += " " * 2 + card.bottom_line()
        
        # Print the card lines
        print(top_border)
        print(top_line)
        print(middle_line)
        print(bottom_line)
        print()
    
    def deal(self):
        self.hand.append(Card(random.randint(1, 13), 
                              random.randint(0, 7)) )

    def get_score(self):
        score = 0

        for card in self.hand:
            # Aces have a rank of 1
            # They can either be 11 or 1
            if (card.value() == 1):
                if ((WINNING_NUMBER - score) >= 11):
                    score += 11
                else:
                    score += 1
            else:
                score += card.value()
         
        return score

# implement the win logic
def get_winner(player, dealer):
    # There are a number of conditions that are possible
    # 1. Both the player and the dealer exceed the winning
    # number aka a double burst
    if (player.get_score() > WINNING_NUMBER and
        dealer.get_score() > WINNING_NUMBER):
        winner = None
    elif player.get_score() > WINNING_NUMBER:
        # Either the player or the dealer are greater than
        # the winning number
        winner = dealer
    elif dealer.get_score() > WINNING_NUMBER:
        winner = player
    elif player.get_score == WINNING_NUMBER:
        winner = player
    elif dealer.get_score == WINNING_NUMBER:
        winner = dealer
    else:
        # The last condition is where both have not
        # exceeded the score
        
        if (abs(WINNING_NUMBER - player.get_score()) < 
                (WINNING_NUMBER - dealer.get_score())):
            winner = player
        elif (abs(WINNING_NUMBER - player.get_score()) > 
                (WINNING_NUMBER - dealer.get_score())):
            winner = dealer
        elif (abs(WINNING_NUMBER - player.get_score()) == 
                (WINNING_NUMBER - dealer.get_score())):
            winner = None
        else:
            winner = None
    
    return winner   

def check_game_over(player, dealer, stand):
    if stand is True:
        return True
    elif (player.get_score() > WINNING_NUMBER or
            dealer.get_score() > WINNING_NUMBER or
            player.get_score() == WINNING_NUMBER or
            dealer.get_score() == WINNING_NUMBER):
        return True

    return False

def main():    
    # Initialise the players
    player = Player("Player") 
    dealer = Player("Dealer") 

    print(r"""
    +==========================================================================+
    | ____    ___                    __                             __         |
    |/\  _`\ /\_ \                  /\ \        __                 /\ \        |
    |\ \ \L\ \//\ \      __      ___\ \ \/'\   /\_\     __      ___\ \ \/'\    |
    | \ \  _ <'\ \ \   /'__`\   /'___\ \ , <   \/\ \  /'__`\   /'___\ \ , <    |
    |  \ \ \L\ \\_\ \_/\ \L\.\_/\ \__/\ \ \\`\  \ \ \/\ \L\.\_/\ \__/\ \ \\`\  |
    |   \ \____//\____\ \__/.\_\ \____\\ \_\ \_\_\ \ \ \__/.\_\ \____\\ \_\ \_\|
    |    \/___/ \/____/\/__/\/_/\/____/ \/_/\/_/\ \_\ \/__/\/_/\/____/ \/_/\/_/|
    |                                          \ \____/                        |
    |                                           \/___/                         |
    +==========================================================================+
    """)

    print(r"""Blackjack, by John Banda, adrielbanda4@gmail.com

        Rules:
          Try to get as close to 21 without going over.
          Kings, Queens, and Jacks are worth 10 points.
          Aces are worth 1 or 11 points.
          Cards 2 through 10 are worth their face value.
          (H)it to take another card.
          (S)tand to stop taking cards.
          On your first play, you can (D)ouble down to increase your bet
          but must hit exactly one more time before standing.
          In case of a tie, the bet is returned to the player.
          The dealer stops hitting at 17.
    """)

    print()

    # Choose amount to bet
    bet = 0
    bet_input = input(f"How much do you bet? (1 - {player.cash}, or QUIT) > ").strip()

    if bet_input.lower() == "quit":
        print("Thanks for playing!")
        sys.exit(0)

    # Otherwise, convert safely
    try:
        bet = min(int(bet_input), player.cash)
    except ValueError:
        sys.exit(1)

    # After the player chooses his bet, show the hands
    player.show_hand()
    dealer.show_hand(True)

    stand       = False
    game_over   = check_game_over(player, dealer, stand)
    double_down = True

    while stand is not True and game_over is not True:

        # Get input. Only double down if this is the first play
        player_input = input("(H)it, (S)stand, (D)double down > ")

        match(player_input.lower()):
            case 'h':
                double_down = False

                player.deal()
                # The dealer stops dealing at 17
                if (dealer.get_score() < 17):
                    dealer.deal()
            case 's':
                stand = True;
            case 'd':
                # The player wants to double down:
                bet = int(input(f"How much do you bet? (1 - {cash}, or QUIT) > "))
            case _:
                print('Unknown input sir!!')

        # After every play, print the current deck
        game_over = check_game_over(player, dealer, stand)
        print(game_over)

        print()
        player.show_hand()
        dealer.show_hand(hide_top_card=(not game_over))

    # if the play was stopped let's determine who the winner is

    if game_over is True:
        # get the winner
        winner = get_winner(player, dealer)

        # Let's start with a draw
        if winner is None:
            print("Game ends in a Draw!!!")
            # Nothing happens to the player's cash
        elif winner.type == "Player":
            print("Player wins!!!! :)")
            player.cash += bet
        else:
            print("Dealer wins!!!! :)")
            player.cash -= bet

# if the program is run (instead of imported, run it:
if __name__ == '__main__':
    main()
