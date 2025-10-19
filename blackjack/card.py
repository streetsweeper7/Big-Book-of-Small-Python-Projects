
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
            symbol = str(self.rank)

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
         

