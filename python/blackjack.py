'''
Practice : Blackjack
Marcel Schaeffer
10/24/17
'''

import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + ' of ' + self.rank

    def value(self):
        if self.rank == 'A':
            return 1
        elif self.rank == 'J' or self.rank == 'Q' or self.rank == 'K' or self.rank == '10':
            return 10
        return int(self.rank)


class Deck:
    def __init__(self):
        self.cards = []
        suits = ['spades', 'diamonds', 'hearts', 'clubs']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        for suit in suits:
            for rank in ranks:
                #print(suit + ' -  ' + rank)
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)
        random.shuffle(self.cards)
        random.shuffle(self.cards)

    def cut(self):
        cut_point = random.randint(4, 46)
        temp_cards = []
        top_cut = self.cards[:cut_point]
        bottom_cut = self.cards[cut_point:]
        bottom_cut.extend(top_cut)
        self.cards = bottom_cut

    def draw_card(self):
        return self.cards.pop(0)


class Hand:
    def __init__(self):
        self.cards = []

    #add card to hand
    def in_hand(self, card):
        self.cards.append(card)

    def print_cards(self):
        for card in self.cards:
            print(card)

    def hand_value(self):
        hand_total = 0
        for card in self.cards:
            hand_total += card.value()
        return hand_total


deck = Deck()
deck.shuffle()
deck.cut()

#deal hand
hand = Hand()
card = deck.draw_card() #draw a card
hand.in_hand(card)
card = deck.draw_card() #draw another card
hand.in_hand(card)
hand.print_cards()
print(hand.hand_value())

command = input('Hit or stay? ').lower()

if command == 'hit':
    card = deck.draw_card()  # draw another card
    hand.in_hand(card)
    hand.print_cards()
    print(hand.hand_value())