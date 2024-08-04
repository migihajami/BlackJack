

class Card:
    name: str
    suit: str
    value: str
    nick: str
    suit_symbol: str

    suit_symbols = {"Hearts": "\u2665", "Clubs": "\u2663", "Diamonds": "\u2666", "Spades": "\u2660"}

    def __init__(self, name, suit, value, nick):
        self.name = name
        self.suit = suit
        self.value = value
        self.nick = nick
        self.suit_symbol = self.suit_symbols[suit]

    def __str__(self):
        return f"[{self.nick}{self.suit_symbol}]"

