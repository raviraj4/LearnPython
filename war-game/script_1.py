import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
class Card:
    def __init__(self, suit, rank):
        self.suit = suit 
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                card_z = Card(suit, rank)
                self.all_cards.append(card_z)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
                
    def __str__(self):
        for suit in suits:
            for rank in ranks:
                card1 = Card(suit, rank)
                print(card1)

    def deal_one(self):
        return self.all_cards.pop()
    

class Player:
    def __init__(self, name):
        self.name = name 
        self.all_cards =[]

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'


# Game setup
p1 = Player("One")
p2 = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26): # because a deck has 52 cards and half of it is 26
    p1.add_cards(new_deck.deal_one())
    p2.add_cards(new_deck.deal_one)

len(p1.all_cards)




# while gameon
    # while at_war


# driver code
        
np = Player("Bochya")    
print(np)
deck1 = Deck()
# print(deck1)
deck1.shuffle()
# print(deck1)
mycard = deck1.deal_one()
# print(mycard)
np.add_cards(mycard)
np.add_cards([mycard, mycard, mycard])
