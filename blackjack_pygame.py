import pygame
import random


pygame.init()
width = 1200
height = 650
screen = pygame.display.set_mode((width, height))
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 24, bold=True)



background_img = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/green.jpg")
clubs_2 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/2 clubs.png")
clubs_3 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/3 clubs.png")
clubs_4 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/4 clubs.png")
clubs_5 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/5 clubs.png")
clubs_6 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/6 clubs.png")
clubs_7 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/7 clubs.png")
clubs_8 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/8 clubs.png")
clubs_9 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/9 clubs.png")
clubs_10 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/10 clubs.png")
clubs_J = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/J clubs.png")
clubs_Q = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/Q clubs.png")
clubs_K = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/K clubs.png")
clubs_A = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/A clubs.png")
diamonds_2 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/2 diamonds.png")
diamonds_3 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/3 diamonds.png")
diamonds_4 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/4 diamonds.png")
diamonds_5 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/5 diamonds.png")
diamonds_6 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/6 diamonds.png")
diamonds_7 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/7 diamonds.png")
diamonds_8 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/8 diamonds.png")
diamonds_9 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/9 diamonds.png")
diamonds_10 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/10 diamonds.png")
diamonds_J = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/J diamonds.png")
diamonds_Q = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/Q diamonds.png")
diamonds_K = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/K diamonds.png")
diamonds_A = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/A diamonds.png")
spades_2 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/2 spades.png")
spades_3 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/3 spades.png")
spades_4 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/4 spades.png")
spades_5 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/5 spades.png")
spades_6 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/6 spades.png")
spades_7 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/7 spades.png")
spades_8 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/8 spades.png")
spades_9 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/9 spades.png")
spades_10 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/10 spades.png")
spades_J = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/J spades.png")
spades_Q = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/Q spades.png")
spades_K = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/K spades.png")
spades_A = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/A spades.png")
hearts_2 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/2 hearts.png")
hearts_3 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/3 hearts.png")
hearts_4 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/4 hearts.png")
hearts_5 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/5 hearts.png")
hearts_6 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/6 hearts.png")
hearts_7 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/7 hearts.png")
hearts_8 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/8 hearts.png")
hearts_9 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/9 hearts.png")
hearts_10 = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/10 hearts.png")
hearts_J = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/J hearts.png")
hearts_Q = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/Q hearts.png")
hearts_K = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/K hearts.png")
hearts_A = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/A hearts.png")
back_card = pygame.image.load("/Users/manossavvides/PycharmProjects/games/venv/bin/projects/blackjack/back card.png")
clubs_2 = pygame.transform.rotozoom(clubs_2, 0, 0.18)
clubs_3 = pygame.transform.rotozoom(clubs_3, 0, 0.18)
clubs_4 = pygame.transform.rotozoom(clubs_4, 0, 0.18)
clubs_5 = pygame.transform.rotozoom(clubs_5, 0, 0.18)
clubs_6 = pygame.transform.rotozoom(clubs_6, 0, 0.18)
clubs_7 = pygame.transform.rotozoom(clubs_7, 0, 0.18)
clubs_8 = pygame.transform.rotozoom(clubs_8, 0, 0.18)
clubs_9 = pygame.transform.rotozoom(clubs_9, 0, 0.18)
clubs_10 = pygame.transform.rotozoom(clubs_10, 0, 0.18)
clubs_J = pygame.transform.rotozoom(clubs_J, 0, 0.18)
clubs_Q = pygame.transform.rotozoom(clubs_Q, 0, 0.18)
clubs_K = pygame.transform.rotozoom(clubs_K, 0, 0.18)
clubs_A = pygame.transform.rotozoom(clubs_A, 0, 0.18)
diamonds_2 = pygame.transform.rotozoom(diamonds_2, 0, 0.18)
diamonds_3 = pygame.transform.rotozoom(diamonds_3, 0, 0.18)
diamonds_4 = pygame.transform.rotozoom(diamonds_4, 0, 0.18)
diamonds_5 = pygame.transform.rotozoom(diamonds_5, 0, 0.18)
diamonds_6 = pygame.transform.rotozoom(diamonds_6, 0, 0.18)
diamonds_7 = pygame.transform.rotozoom(diamonds_7, 0, 0.18)
diamonds_8= pygame.transform.rotozoom(diamonds_8, 0, 0.18)
diamonds_9 = pygame.transform.rotozoom(diamonds_9, 0, 0.18)
diamonds_10 = pygame.transform.rotozoom(diamonds_10, 0, 0.18)
diamonds_J = pygame.transform.rotozoom(diamonds_J, 0, 0.18)
diamonds_Q = pygame.transform.rotozoom(diamonds_Q, 0, 0.18)
diamonds_K = pygame.transform.rotozoom(diamonds_K, 0, 0.18)
diamonds_A = pygame.transform.rotozoom(diamonds_A, 0, 0.18)
spades_2 = pygame.transform.rotozoom(spades_2, 0, 0.18)
spades_3 = pygame.transform.rotozoom(spades_3, 0, 0.18)
spades_4 = pygame.transform.rotozoom(spades_4, 0, 0.18)
spades_5 = pygame.transform.rotozoom(spades_5, 0, 0.18)
spades_6 = pygame.transform.rotozoom(spades_6, 0, 0.18)
spades_7 = pygame.transform.rotozoom(spades_7, 0, 0.18)
spades_8 = pygame.transform.rotozoom(spades_8, 0, 0.18)
spades_9 = pygame.transform.rotozoom(spades_9, 0, 0.18)
spades_10 = pygame.transform.rotozoom(spades_10, 0, 0.18)
spades_J = pygame.transform.rotozoom(spades_J, 0, 0.18)
spades_Q = pygame.transform.rotozoom(spades_Q, 0, 0.18)
spades_K = pygame.transform.rotozoom(spades_K, 0, 0.18)
spades_A = pygame.transform.rotozoom(spades_A, 0, 0.18)
hearts_2 = pygame.transform.rotozoom(hearts_2, 0, 0.18)
hearts_3 = pygame.transform.rotozoom(hearts_3, 0, 0.18)
hearts_4 = pygame.transform.rotozoom(hearts_4, 0, 0.18)
hearts_5 = pygame.transform.rotozoom(hearts_5, 0, 0.18)
hearts_6 = pygame.transform.rotozoom(hearts_6, 0, 0.18)
hearts_7 = pygame.transform.rotozoom(hearts_7, 0, 0.18)
hearts_8 = pygame.transform.rotozoom(hearts_8, 0, 0.18)
hearts_9 = pygame.transform.rotozoom(hearts_9, 0, 0.18)
hearts_10 = pygame.transform.rotozoom(hearts_10, 0, 0.18)
hearts_J = pygame.transform.rotozoom(hearts_J, 0, 0.18)
hearts_Q = pygame.transform.rotozoom(hearts_Q, 0, 0.18)
hearts_K = pygame.transform.rotozoom(hearts_K, 0, 0.18)
hearts_A = pygame.transform.rotozoom(hearts_A, 0, 0.18)
back_card = pygame.transform.rotozoom(back_card, 0, 0.235)



class Deck:
   def __init__(self):
       self.deck = [hearts_2, hearts_3, hearts_4, hearts_5, hearts_6, hearts_7, hearts_8, hearts_9, hearts_10, hearts_J,
                    hearts_Q, hearts_K, hearts_K, clubs_2, clubs_3, clubs_4, clubs_5, clubs_6, clubs_7,clubs_8, clubs_9,
                    clubs_10, clubs_J, clubs_Q, clubs_K, clubs_A, diamonds_2, diamonds_3, diamonds_4, diamonds_5, diamonds_6, diamonds_7,
                    diamonds_8, diamonds_9, diamonds_10, diamonds_J, diamonds_Q, diamonds_K, diamonds_A, spades_2, spades_3, spades_4,
                    spades_5, spades_6, spades_7, spades_8, spades_9, spades_10, spades_J, spades_Q, spades_K, spades_A,]

       random.shuffle(self.deck)



class Player:
    def __init__(self, name):
        self.hand = 0
        self.won = False
        self.lost = False
        self.tie = False
        self.cards = []
        self.name = name
        self.show_cards = False
        self.cards.append(deck1.deck.pop())
        self.cards.append(deck1.deck.pop())
        self.calculate_hand()


    def draw_player(self, win):
        x = 100
        y = 350
        i = 160
        for card in self.cards:
            win.blit(card, (x , y))
            x += i

    def draw_dealer(self, win):
        if not self.show_cards:
            x = 100
            y = 80
            win.blit(self.cards[0], (x, y))
            win.blit(back_card, (240, 70))
        else:
            x = 100
            y = 80
            i = 160
            for card in self.cards:
                win.blit(card, (x , y))
                x += i


    def calculate_hand(self):
        for card1 in self.cards:
            if card1 == spades_2 or card1 == hearts_2 or card1 == clubs_2 or card1 == diamonds_2:
                self.hand += 2
            elif card1 == spades_3 or card1 ==  hearts_3 or card1 == clubs_3 or card1 == diamonds_3:
                self.hand += 3
            elif card1 == spades_4 or card1 == hearts_4 or card1 == clubs_4 or card1 == diamonds_4:
                self.hand += 4
            elif card1 == spades_5 or card1 == hearts_5 or card1 == clubs_5 or card1 == diamonds_5:
                self.hand += 5
            elif card1 == spades_6 or card1 == hearts_6 or card1 == clubs_6 or card1 == diamonds_6:
                self.hand += 6
            elif card1 == spades_7 or card1 == hearts_7 or card1 == clubs_7 or card1 == diamonds_7:
                self.hand += 7
            elif card1 == spades_8 or card1 == hearts_8 or card1 == clubs_8 or card1 == diamonds_8:
                self.hand += 8
            elif card1 == spades_9 or card1 == hearts_9 or card1 == clubs_9 or card1 == diamonds_9:
                self.hand += 9
            elif card1 == spades_10 or card1 == hearts_10 or card1 == clubs_10 or card1 == diamonds_10:
                self.hand += 10
            elif card1 == spades_J or card1 == hearts_J or card1 == clubs_J or card1 == diamonds_J:
                self.hand += 10
            elif card1 == spades_Q or card1 == hearts_Q or card1 == clubs_Q or card1 == diamonds_Q:
                self.hand += 10
            elif card1 == spades_K or card1 == hearts_K or card1 == clubs_K or card1 == diamonds_K:
                self.hand += 10
            else:
                if self.hand >= 11:
                    self.hand += 1
                else:
                    self.hand += 11

        return self.hand

    def add_card(self):
        self.cards.append(deck1.deck.pop())
        self.hand = 0
        self.calculate_hand()
        calculate_winner()


def restart():
    res = myfont.render(" Q to restart", True, (0, 0, 0))
    screen.blit(res, (600, 300))



def redraw_window():
    player1.draw_player(screen)
    dealer.draw_dealer(screen)
    pygame.draw.rect(screen, (248,248,255),(120,570,100,25))
    pygame.draw.rect(screen, (248, 248, 255), (277, 570, 100, 25))
    hit_button = myfont.render('HIT', True, (0, 0, 0))
    screen.blit(hit_button, (143, 565))
    stay_button = myfont.render('STAY', True, (0, 0, 0))
    screen.blit(stay_button, (290, 565))
    dealer_cards = myfont.render("DEALER'S CARDS", True, (0, 0, 0))
    screen.blit(dealer_cards, (140, 25))
    score = myfont.render(f"Sum is {player1.hand}", True, (0, 0, 0))
    screen.blit(score, (500, 600))

    if dealer.won:
        won = myfont.render("DEALER HAS WON", True, (0, 0, 0))
        screen.blit(won, (500, 300))

    elif player1.won:
        won = myfont.render("PLAYER HAS WON", True, (0, 0, 0))
        screen.blit(won, (500, 300))

    if dealer.lost:
        lost = myfont.render("DEALER HAS LOST", True, (0, 0, 0))
        screen.blit(lost, (500, 300))

    elif player1.lost:
        lost = myfont.render("PLAYER HAS LOST", True, (0, 0, 0))
        screen.blit(lost, (500, 300))
    elif dealer.tie:
        tie =  myfont.render("IT'S A TIE", True, (0, 0, 0))
        screen.blit(tie, (500, 300))


    pygame.display.update()


def calculate_winner():
    if dealer.hand == 21:
        dealer.show_cards = True
        dealer.won = True
        dealer.draw_dealer(screen)

    if player1.hand == 21:
        player1.won = True

    if player1.hand > 21:
        player1.lost = True

    if dealer.hand > 21:
        dealer.lost = True


def cal_winner():
    if dealer.hand > player1.hand:
        dealer.won = True
    if dealer.hand == player1.hand:
        dealer.tie = True
    if player1.hand < dealer.hand:
        dealer.won = True


run = True

deck1 = Deck()
player1 = Player("player")
dealer = Player("dealer")
calculate_winner()



while run:
    screen.blit(background_img, (0, 0))
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if 220 > mouse[0] > 120 and 594 > mouse[1] > 570:
             if event.type == pygame.MOUSEBUTTONUP:
                 player1.add_card()
        if 377 > mouse[0] > 277 and 594 > mouse[1] > 570:
            if event.type == pygame.MOUSEBUTTONUP:
                dealer.show_cards = True
                while dealer.hand < player1.hand or (dealer.hand == player1.hand and dealer.hand <= 17):
                    dealer.add_card()
                    dealer.draw_dealer(screen)
                else:
                    calculate_winner()
                    if player1.won == False and dealer.won == False and player1.lost == False and dealer.lost == False:
                        cal_winner()

    redraw_window()

