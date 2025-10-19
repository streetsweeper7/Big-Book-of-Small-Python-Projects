#!/usr/bin/python3
import random
import sys

from player import Player
from card import Card
from deck import Deck

# The game starts with 5000 cash
game_over = False
winner    = 0

class Blackjack():
    winning_number = 21

    def __init__(self):
        self.stand       = False
        self.game_over   = False
        self.double_down = True
        self.player_bet  = 0

    # implement the win logic
    def evaluate_winner(self, player, dealer):
        ''' Returns which winner won the game '''
        player_score = player.get_score()
        dealer_score = dealer.get_score()

        # There are a number of conditions that are possible
        # 1. Both the player and the dealer exceed the winning
        # number aka a double burst
        if (player_score > Blackjack.winning_number and
            dealer_score > Blackjack.winning_number):
            winner = None
        elif player_score > Blackjack.winning_number:
            # Either the player or the dealer are greater than
            # the winning number
            winner = dealer
        elif dealer_score > Blackjack.winning_number:
            winner = player
        elif player_score == Blackjack.winning_number:
            winner = player
        elif dealer_score == Blackjack.winning_number:
            winner = dealer
        else:
            # The last condition is where both have not
            # exceeded the score
            
            if (abs(Blackjack.winning_number - player_score) < 
                    (Blackjack.winning_number - dealer_score)):
                winner = player
            elif (abs(Blackjack.winning_number - player_score) > 
                    (Blackjack.winning_number - dealer_score)):
                winner = dealer
            elif (abs(Blackjack.winning_number - player_score) == 
                    (Blackjack.winning_number - dealer_score)):
                winner = None
            else:
                winner = None
        
        return winner   

    def check_game_over(self, player, dealer, stand):
        ''' Checks if the game is over '''
        if stand:
            return True
        elif (player.get_score() > Blackjack.winning_number or
                dealer.get_score() > Blackjack.winning_number or
                player.get_score() == Blackjack.winning_number or
                dealer.get_score() == Blackjack.winning_number):
            return True

            return False
    
    def make_bet(self, player):

        # Otherwise, convert safely
        while True:
            try:
                bet_input = input(f"How much do you bet? "
                                   "(1 - {player.cash}, "
                                   "or QUIT) > ").strip()

                if bet_input.lower() == "quit":
                    print("Thanks for playing!")
                    sys.exit(1)

                bet = min(int(bet_input), player.cash)
                self.player_bet = bet
                break
            except ValueError:
                bet = 0
        

    def play_round(self, player, dealer, deck):

        # Choose amount to bet
        self.make_bet(player)

        # After the player chooses his bet, show the hands
        player.show_hand()
        dealer.show_hand(True)

        self.stand       = False
        self.game_over   = self.check_game_over(player, dealer, stand)
        self.double_down = True

        while self.stand is not True and self.game_over is not True:

            # Get input. Only double down if this is the first play
            player_input = input("(H)it, (S)stand, (D)double down > ")

            match(player_input.lower()):
                case 'h':
                    self.double_down = False

                    player.deal(deck.deal_card())
                    # The dealer stops dealing at 17
                    if (dealer.get_score() < 17):
                        dealer.deal(deck.deal_card())
                case 's':
                    stand = True
                case 'd':
                    # The player wants to double down:
                    self.make_bet(player)
                case _:
                    print('Unknown input sir!!')

            # After every play, print the current deck
            self.game_over = self.check_game_over(player, dealer, stand)

            print()
            player.show_hand()
            dealer.show_hand(hide_top_card=(not game_over))


    def print_banner(self):
        print(r"""
         ____  _            _     _            _    
        | __ )| | __ _  ___| | __(_) __ _  ___| | __
        |  _ \| |/ _` |/ __| |/ /| |/ _` |/ __| |/ /
        | |_) | | (_| | (__|   < | | (_| | (__|   < 
        |____/|_|\__,_|\___|_|\_\/ |\__,_|\___|_|\_\
                               |__/                 
        """)

    def print_instructions(self):
        ''' Prints the instructions of the game '''
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



def main():    

    # Initialise the players
    game   = Blackjack()
    player = Player("Player") 
    dealer = Player("Dealer") 
    deck   = Deck()
    print()

    # Print the banner and instructions
    game.print_banner()
    print()
    game.print_instructions()

    # Play a round of blackjack
    game.play_round(player, dealer, deck) 

    # Check the result of the round
    if game.game_over:
        # get the winner
        winner = game.evaluate_winner(player, dealer)

        # Let's start with a draw
        if winner is None:
            print("Game ends in a Draw!!!")
            # Nothing happens to the player's cash
        elif winner.type == "Player":
            print("Player wins!!!! :)")
            player.cash += game.player_bet
        else:
            print("Dealer wins!!!! :)")
            player.cash -= game.player_bet


# if the program is run (instead of imported, run it:
if __name__ == '__main__':
    main()
