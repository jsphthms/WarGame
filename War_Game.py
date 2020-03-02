# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = "H D S C".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()


class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    "A" > "K" > "Q" > "J" > "10" > "9" > "8" > "7" > "6" > "5" > "4" > "3" > "2"
    #  Create a deck
    def __init__(self, suite, ranks, deck=[]):
        self.suite = suite
        self.ranks = ranks
        self.deck = deck
        ranks = (
            "A" > "K" > "Q" > "J" > "10" > "9" > "8" > "7" > "6" > "5" > "4" > "3" > "2"
        )

    def make_deck(self):
        deck = []
        for r in self.ranks:
            for s in self.suite:
                card = zip(r, s)
                deck += card
        return deck

    # Shuffle deck of cards
    def shuffle_deck(self, deck: list):
        shuffled_deck = deck
        # shuffled_deck = self.make_deck()
        shuffle(shuffled_deck)
        return shuffled_deck

    # Split deck into 2 parts of 26
    def split_deck(self, deck: list):
        full_deck = deck
        deck1 = full_deck[: len(full_deck) // 2]
        deck2 = full_deck[len(full_deck) // 2 :]
        return deck1, deck2


class Hand:
    """
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    """

    def add(self, cards):
        self.deck.append(tuple(cards))
        return self.deck

    def remove(self, cards):
        self.deck.remove(tuple(cards))
        return self.deck

    def toBottom(self, card):
        self.deck.remove(card)
        self.deck.append(card)
        return self.deck


class Player(Hand):
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """

    def __init__(self, player_name, deck: list):
        Hand.__init__(self)
        self.player_name = player_name
        self.deck = deck

    def draw(self, index):
        draw = self.deck[index]
        return draw

    def check_hand(self):
        print(f"{self.player_name} has {len(self.deck)} cards.")


######################
#### GAME PLAY #######
######################

print("Welcome to War, let's begin...")

print("Creating New Ordered Deck")
deck = Deck(SUITE, RANKS)
ndeck = deck.make_deck()

print("Shuffling and Splitting Deck")
shuffled_deck = deck.shuffle_deck(ndeck)
deck1, deck2 = deck.split_deck(shuffled_deck)[0], deck.split_deck(shuffled_deck)[1]

# Created Computer as player
player1 = Player("Computer", deck1)
# Create player 2
playername = input("What is your name? ")
player2 = Player(playername, deck2)

turns = 0


for i in player1.deck:
    for i in player2.deck:
        if len(player1.deck) != 52 or len(player2.deck) != 52:
            print("It is time for a new round!")
            print("Here are the current standings:\n")
            player1.check_hand()
            player2.check_hand()
            print("Both players play a card!\n")

            print(("{} has placed: {}\n").format(player1.player_name, player1.draw(0)))
            print(("{} has placed: {}\n").format(player2.player_name, player2.draw(0)))
            if player1.draw(0) > player2.draw(0):
                print("Computer has the higher card, adding to hand.")
                player1.toBottom(player1.draw(0))
                player1.add(player2.draw(0))
                player2.remove(player2.draw(0))
            elif player2.draw(0) > player1.draw(0):
                print(f"{playername} has the higher card, adding to hand.")
                player2.toBottom(player2.draw(0))
                player2.add(player1.draw(0))
                player1.remove(player1.draw(0))
            elif player2.draw(0) == player1.draw(0):
                print("We have a match, time for war!")
                print(
                    ("{} has placed: {}\n").format(player1.player_name, player1.draw(4))
                )
                print(
                    ("{} has placed: {}\n").format(player2.player_name, player2.draw(4))
                )
                if player1.draw(4) > player2.draw(4):
                    print("Computer has the higher card, adding to hand.")
                    for i in deck1[0:5]:
                        player1.toBottom(i)
                    for i in deck2[0:5]:
                        player1.add(i)
                    for i in deck2[0:5]:
                        player2.remove(i)
                elif player2.draw(4) > player1.draw(4):
                    print(f"{playername} has the higher card, adding to hand.")
                    for i in deck2[0:5]:
                        player2.toBottom(i)
                    for i in deck1[0:5]:
                        player2.add(i)
                    for i in deck1[0:5]:
                        player1.remove(i)
                elif player2.draw(4) == player1.draw(4):
                    print("We have a match, time for war!")
                    print(
                        ("{} has placed: {}\n").format(
                            player1.player_name, player1.draw(8)
                        )
                    )
                    print(
                        ("{} has placed: {}\n").format(
                            player2.player_name, player2.draw(8)
                        )
                    )
                    if player1.draw(8) > player2.draw(8):
                        print("Computer has the higher card, adding to hand.")
                        for i in deck1[0:9]:
                            player1.toBottom(i)
                        for i in deck2[0:9]:
                            player1.add(i)
                        for i in deck2[0:9]:
                            player2.remove(i)
                    elif player2.draw(8) > player1.draw(8):
                        print(f"{playername} has the higher card, adding to hand.")
                        for i in deck2[0:9]:
                            player2.toBottom(i)
                        for i in deck1[0:9]:
                            player2.add(i)
                        for i in deck1[0:9]:
                            player1.remove(i)
            turns += 1

print(f"GAME OVER\nIt lasted {turns} turns.")
