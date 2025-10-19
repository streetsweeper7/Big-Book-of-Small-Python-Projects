import pytest
from blackjack import Card

def test_card_value_ace_and_face_cards():
    ace = Card(rank=1, suit=0)
    assert ace.value() == 1  # or 11 depending on your logic

    king = Card(rank=13, suit=1)
    assert king.value() == 10

    seven = Card(rank=7, suit=2)
    assert seven.value() == 7

