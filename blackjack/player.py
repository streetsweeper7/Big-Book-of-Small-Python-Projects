from deck import Deck
from card import Card

# Player class
class Player():

    def __init__(self, type, deck: Deck):
        self.cash = 5000    # The player's initial cash
        self.type = type
        self.hand = [deck.deal_card()
                     for _ in range(0, 2)]

    def show_hand(self, hide_top_card=False):
        print()
        
        if hide_top_card:
            print(f"{self.type}: ###")
        else:
            print(f"{self.type}: {self.get_score()}")

        top_border  = ''
        top_line    = ''
        middle_line = ''
        bottom_line = ''

        for i, card in enumerate(self.hand):
            if i == (len(self.hand) - 1) and hide_top_card:
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
    
    def deal(self, card: Card):
        self.hand.append(card)

    def get_score(self, winning_number=21):
        score = 0

        for card in self.hand:
            # Aces have a rank of 1
            # They can either be 11 or 1
            if (card.value() == 1):
                if ((winning_number - score) >= 11):
                    score += 11
                else:
                    score += 1
            else:
                score += card.value()
         
        return score

