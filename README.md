# Cardgame-War

Automatic simulation of the card game War

Uses code from my DeckOfCards repository and pygame

## Rules
Both players draw a card from their deck, and the values are compared. Whichever player has the higher value gets both cards in their discard pile.

If both cards are equal, War occurs, where both players draw 1 card face down, then they draw another card, and the values of that second card are compared. Whichever player has the higher value gets all the cards in their discard pile.

If a player runs out of cards in their deck, their discard pile is shuffled and used.

If a player runs out of cards in both their deck and their discard pile, they lose
