import random


def main():
    class Deck:
        def __init__(self):
            self.deck = ["2","3","4","5","6","7","8","9","J","Q","K","A",
                      "2","3","4","5","6","7","8","9","J","Q","K","A",
                      "2","3","4","5","6","7","8","9","J","Q","K","A",
                      "2","3","4","5","6","7","8","9","J","Q","K","A"]

            random.shuffle(self.deck)

    deck1 = Deck()                 #  create and shuffle deck

    class Player:
        def __init__(self, name):
            self.hand = 0
            self.cards = []
            self.name = name
            self.show_cards = True
            self.cards.append(deck1.deck.pop())
            self.cards.append(deck1.deck.pop())
            self.calculate_hand()
            self.printing()
            self.cal_winner()      # add 2 cards to the dealer and the player prints their cards and if check if hit blackjack

        def printing(self):
            if self.show_cards:
                if self.name == "player1":
                    print(f"{self.name} cards are {self.cards} ({self.hand}) ")
                else:
                    print(f"{self.name} cards are ['{self.cards[0]}, '?'] ")
            else:
                print(f"{self.name} cards are {self.cards} ({self.hand}) ")    # prints player's card and dealer's cards


        def add_card(self):
            self.cards.append(deck1.deck.pop())
            self.hand = 0
            self.calculate_hand()
            self.printing()             # adds cards to the player or the dealer and calculates the sum of their cards. Prints again their score and 
                                        #cards

        def calculate_hand(self):
            for card in self.cards:
                if card in "23456789":
                    self.hand += int(card)
                elif card in "JQK":
                    self.hand += 10
                elif card in "A":
                    if self.hand >= 11:
                        self.hand += 1
                    else:
                        self.hand += 11
            return self.hand                # calculates the sum of player's and dealer's cards


        def cal_winner(self):
            if self.hand == 21:
                print(f"{self.name} has  WON")
                main()
            if self.hand > 21:
                print(f"{self.name}  has LOST")
                main()                             # checks if hit blackjack or over 21



    player1 = Player("player1")
    dealer = Player("dealer")


    def calculate_winner():
        if dealer.hand > player1.hand:
            print(f"{dealer.name} has  WON")
            main()
        if dealer.hand == player1.hand:
            print("IT'S A TIE")
            main()
        if player1.hand < dealer.hand:
            print(f"{player1.name} has LOST")
            main()                                       # checks who won between player and dealer


    answer = "hit"
    while answer == "hit":
        print("Do you want to hit or stay")
        answer = input()
        if answer == "hit":
            player1.add_card()
            player1.cal_winner()
        else:
            dealer.show_cards = False
            player1.printing()
            while dealer.hand<player1.hand or (dealer.hand==player1.hand and dealer.hand<=17):
                dealer.add_card()
            else:
                dealer.cal_winner()
                calculate_winner()
                                             # loop which player hits or stands and then dealer cards are added. It decides the winner based with 
                                             # the previous functions
main()




