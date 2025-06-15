# deck2.py
"""Card and Deck classes for simulating a card game."""

import random

class Card:
    """A playing card with a rank and suit."""
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __repr__(self):
        return f"{self.face} of {self.suit}"

class Deck:
    """A standard deck of 52 playing cards."""
    faces = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
             'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self):
        self._deck = [Card(face, suit) for suit in self.suits for face in self.faces]
        self._current_card = 0

    def shuffle(self):
        random.shuffle(self._deck)
        self._current_card = 0

    def deal_card(self):
        if self._current_card < len(self._deck):
            card = self._deck[self._current_card]
            self._current_card += 1
            return card
        else:
            raise ValueError("All cards have been dealt.")

    def __repr__(self):
        return f"Deck of {len(self._deck) - self._current_card} remaining cards."

# Run only when this file is executed directly
if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    for i in range(5):
        print(deck.deal_card())
    print(deck)
