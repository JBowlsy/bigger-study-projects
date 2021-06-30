#blackjack with help

import random
import time

class Card():
    """simulate  single card with rank, value, and suit"""
    def __init__(self, rank, value, suit):
        self.rank = rank  #Ace, king etc
        self.value = value # 1-10, 11
        self.suit = suit

    def display_card(self):
        """Show rank and suit of card"""
        print(self.rank + " of " + self.suit)

    
class Deck():
    """Create deck of 52 cards"""
    def __init__(self):
        self.cards = []

    def build_deck(self):
        """Create 52 card deck"""
        suits = ["Hearts", "Clubs", "Spades", "Diamonds"]
        ranks = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9,
                 "10":10, "Jack":10, "Queen":10, "King":10, "Ace":11,}
        for suit in suits:
            for rank, value in ranks.items():
                card = Card(rank, value, suit)
                self.cards.append(card)
    
    def shuffle_deck(self):
        """Shuffle a deck of cards"""
        random.shuffle(self.cards)
        
    
    def deal_card(self):
        """Remove card from deck and deal it"""
        card = self.cards.pop()
        return card

        

class Player():
    """A class for user to play blackjack"""
    def __init__(self):
        self.hand = [] #a list holding the players cards
        self.hand_value = 0  #total value of players cards
        self.playing_hand = True   #track if player is playing hand

    def draw_hand(self, deck):
        """Deal the players first hand"""
        for i in range(2):
            card = deck.deal_card()
            self.hand.append(card)

    def display_hand(self):
        """Show the player what cards they have"""
        print("\nPlayer's hand: ")
        for card in self.hand:
            card.display_card()

    
    def hit(self, deck):
        """Give the player another card"""
        card = deck.deal_card()
        self.hand.append(card)
        
    def get_hand_value(self):
        """get the value of the cards the player has"""
        self.hand_value = 0
        ace_in_hand = False
        for card in self.hand:
            self.hand_value += card.value
            if card.rank == "Ace":
                ace_in_hand = True
        if self.hand_value > 21 and ace_in_hand:
            self.hand_value -= 10
        print("Value: " + str(self.hand_value))
        
    def update_hand(self, deck):
        """take cards as long as players hand is under 21"""
        if self.hand_value < 21:
            hit_me = input("\nWould you like to hit (y/n): ").lower()
            if hit_me == "y":
                self.hit(deck)
            else:
                self.playing_hand = False
        else:
            self.playing_hand = False


class Dealer():
    """Simulation of the dealer"""
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.playing_hand = True

    def draw_hand(self, deck):
        """get first 2 cards for the dealers first hand"""
        for i in range(2):
            card = deck.deal_card()
            self.hand.append(card)

    def display_hand(self):
        """Show the dealers cards"""
        input("\nPress enter to reveal dealer cards: ")
        for card in self.hand:
            card.display_card()
            time.sleep(1)

    def hit(self, deck):
        """continue to Hit while under 17"""
        self.get_hand_value()
        while self.hand_value < 17:
            card = deck.deal_card()
            self.hand.append(card)
            self.get_hand_value()
        print("\nThere are " + str(len(self.hand)) + " cards in the dealers hand")

    def get_hand_value(self):
        """record the value for the dealers hand and check for an ace"""
        self.hand_value = 0
        ace_in_hand = False
        for card in self.hand:
            self.hand_value += card.value
            if card.rank == "Ace":              #check for an Ace
                ace_in_hand = True
        if self.hand_value > 21 and ace_in_hand:    #change Ace value to 1
            self.hand_value -= 10


class Game():
    """Simulation of the game"""
    def __init__(self, money):
        self.money = int(money) #Total money the player is using
        self.bet = 20
        self.winner = ""

    def set_bet(self):
        """placing the players bet"""
        betting = True
        while betting:
            bet = int(input("How much would you like to bet: "))
            if bet < 20:
                bet = 20
            if bet > self.money:
                print("You cannot afford that amount")
            else: 
                self.bet = bet
                betting = False

    def scoring(self, players_hv, dealers_hv):   #hv = hand_value
        if players_hv == 21:
            print("\nYou got Blackjack!!!!")
            self.winner = "p"
        elif dealers_hv == 21:
            print("\nDealer got Blackjack.")
            self.winner = "d"
        elif players_hv > 21:
            print("\nYou went bust")
            self.winner = "d"
        elif dealers_hv > 21:
            print("\nDealer went bust!!")
            self.winner = "p"
        else:
            if players_hv > dealers_hv:
                print("\nPlayers hand: " + str(players_hv)
                + "\n\nDealers hand: " + str(dealers_hv))
                self.winner = "p"
            elif dealers_hv > players_hv:
                print("\nPlayers hand: " + str(players_hv)
                + "\n\nDealers hand: " + str(dealers_hv))
                self.winner = "d"
            else:
                players_hv = dealers_hv
                print("\nPlayers hand: " + str(players_hv)
                + "\n\nDealers hand: " + str(dealers_hv))
                self.winner = "tie"

    def payout(self):
        if self.winner == "p":
            self.money += self.bet
        elif self.winner == "d":
            self.money -= self.bet

    def display_money(self):
        print("\nYour money: " + str(self.money))

    def display_money_and_bet(self):
        print("\nCurrent money: " + str(self.money) + "\nCurrent bet " + str(self.bet))

print("\nWelcome to the blackjack application")
print("\nThe minimum bet is 20 euros")
money = int(input("How much would you like to start with: "))
game = Game(money)

playing = True
while playing:
    """create and shuffle the deck"""
    game_deck = Deck()
    game_deck.build_deck()   #method so it doesn't need a variable for object name
    game_deck.shuffle_deck()  #same

    """Create the player and dealer"""
    player = Player()
    dealer = Dealer()

    """Display how much money the game has"""
    game.display_money()
    game.set_bet()

    """Draw cards"""
    player.draw_hand(game_deck)
    dealer.draw_hand(game_deck)

    """Display game money"""
    game.display_money_and_bet()
    print("The dealer has a " + dealer.hand[0].rank + " of " 
    + dealer.hand[0].suit)

    """Player gets there cards"""
    while player.playing_hand:
        player.display_hand()
        player.get_hand_value()
        player.update_hand(game_deck)
    
    """dealer keeps going til they hit 17 and then shows their hand"""
    dealer.hit(game_deck)
    dealer.display_hand()

    """Score the game and give the winner their money"""
    game.scoring(player.hand_value, dealer.hand_value)
    game.payout()

    if game.money < 20:
        playing = False
        print("\nYou don't have enough money to continue")


