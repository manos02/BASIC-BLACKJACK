
#create deck
#shuffle cards
#give one card to the player then to the dealer and then again to the player and one to the dealer faced up
#player decides if he wants to hit or stay
#if you hit and go over 21 you bust regardless the dealer's cards / if you hit 21 you win
#then if the cards of the dealer are lower than 17 he has to hit

import random

def main():
    deck = ["2","3","4","5","6","7","8","9","10","J","Q","K","A",
            "2","3","4","5","6","7","8","9","10","J","Q","K","A",
            "2","3","4","5","6","7","8","9","10","J","Q","K","A",
            "2","3","4","5","6","7","8","9","10","J","Q","K","A"]

    player_cards = []
    dealer_cards = []


    random.shuffle(deck)


    player_cards.append(deck[0])
    player_cards.append(deck[1])
    dealer_cards.append(deck[7])
    dealer_cards.append(deck[8])


    print("player has ", player_cards)
    print("dealer has ", dealer_cards[0], "X")

    try:
        p_cards = int(player_cards[0]) + int(player_cards[1])
    except:
        try:
            p_cards = int(player_cards[0]) + 10
            if player_cards[1] == "A":
                p_cards += 1
        except:
            try:
                p_cards = int(player_cards[1]) + 10
                if player_cards[0] == "A":
                    p_cards += 1
            except:
                p_cards = 20
                if player_cards[0] == "A" or player_cards[1] == "A":
                    p_cards = 21
                if player_cards[0] == "A" and player_cards[1] == "A":
                    p_cards = 12


    try:
        d_cards = int(dealer_cards[0]) + int(dealer_cards[1])
    except:
        try:
            d_cards = int(dealer_cards[0]) + 10
            if dealer_cards[1] == "A":
                d_cards += 1
        except:
            try:
                d_cards = int(dealer_cards[1]) + 10
                if dealer_cards[0] == "A":
                    d_cards += 1
            except:
                d_cards = 20
                if dealer_cards[0] == "A" or dealer_cards[1] == "A":
                    d_cards = 21
                if dealer_cards[0] == "A" and dealer_cards[1] == "A":
                    d_cards = 12


    if d_cards != 21:
        if p_cards == 21:
            print("YOU WON")
            main()
    else:
        if p_cards != 21:
            print(dealer_cards)
            print("YOU LOST")
            main()
        else:
            print("TIE")
            main()


    answer = "hit"
    i = 3
    x = 2
    a = 9
    b = 2

    while answer == "hit":
        print("Do you want to hit or stay? ")
        answer = input()
        if answer == "hit":
            player_cards.append(deck[i])
            print("player has ", player_cards)
            try:
                 p_cards += int(player_cards[x])

            except:
                 p_cards += 10
                 if player_cards[0] and dealer_cards[1] and player_cards[2] == "A":
                    p_cards = 13

                 if player_cards[x] == "A":
                     if 21 - p_cards > 11:
                         p_cards += 11
                     else:
                         p_cards += 1

            x += 1
            i += 1
            if p_cards > 21:
                print("YOU LOST")
                main()
            if p_cards == 21:
                print("YOU WON")
                main()


        else:
            print(player_cards)
            print(dealer_cards)
            if d_cards == 21 or d_cards > p_cards:
                print("YOU LOST")
                main()

            while d_cards < 17 or d_cards<p_cards:
                dealer_cards.append(deck[a])
                print("dealer has", dealer_cards)
                try:
                    d_cards += int(dealer_cards[b])
                except:
                    d_cards += 10
                    if dealer_cards[b] == "A":
                        if 21-d_cards > 11:
                            d_cards += 11
                        else:
                            d_cards += 1


                print(d_cards)

                b += 1
                a += 1
            if d_cards > 21:
                print("YOU WON")
                main()
            if p_cards > d_cards:
                print("YOU WON")
                main()
            elif p_cards == d_cards:
                print("TIE")
                main()
            else:
                print("YOU LOST")
                main()


if __name__ == '__main__':
    main()


