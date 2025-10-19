import random

# Create a deck class
class Deck():
    def __init__(self):
        self.ranks = range(1, 14)
        self.suits = range(0, 4)
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(self.cards)
    
    def deal_card(self):
        """Remove and return one card from the deck."""
        if not self.cards:
            raise ValueError("No more cards in the deck!")
        return self.cards.pop() 
