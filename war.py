from turtle import width
from card import *
from deck import Deck
from image_creator import *
import pygame
import time


# def CreateCard(card):
#     new_card = pygame.image.load("images/card_base.png")
#     new_card.blit(pygame.image.load("images/card_" + str(card.get_suit()).lower() + ".png"), (0,0))
#     new_card.blit(pygame.image.load("images/card_" + str(card.get_val()).lower() + ".png"), (0,0))
#     return new_card

# initialize decks
player1_deck = Deck()
player2_deck = Deck()
player1_discard = Deck()
player2_discard = Deck()
saved_cards = Deck()

# generate the deck and split
player1_deck.gen_deck(card_vals = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"], card_counts = [4,4,4,4,4,4,4,4,4,4,4,4,4])
player1_deck.shuffle()
player2_deck.insert_cards(player1_deck.draw(26))
player1_deck.shuffle()
player2_deck.shuffle()

# create card compare object
card_comp = CardCompare()

# create card drawer
card_creator = CardImageCreator()


#initialize pygame
pygame.init()
pygame.display.init()

# Initilize the display
gameDisplay = pygame.display.set_mode((800, 800))

# Load the board image and display it
board_img = pygame.image.load("images/board.png")
gameDisplay.blit(board_img, (0,0))

# Load the banner(s)
banner_img = pygame.image.load("images/banner.png")
player_banner = pygame.image.load("images/player_disp.png")
to_win_banner = pygame.image.load("images/banner_to_win.png")

# create the fonts
blue = (72, 0, 255)
font = pygame.font.Font('freesansbold.ttf', 60)
font2 = pygame.font.Font('freesansbold.ttf', 32)

# Banner text
text = font.render("", True, blue)
textRect = text.get_rect()
textRect.center = ((banner_img.get_rect().width )//2+ 30, (banner_img.get_rect().height )//2+ 33)

# player text
text_p1 = font2.render("", True, blue)
text_p2 = font2.render("", True, blue)
textRect_p1 = text_p1.get_rect()
textRect_p1.center = ((player_banner.get_rect().width )//2+ 75, (player_banner.get_rect().height )//2+ 600)
textRect_p1 = text_p2.get_rect()
textRect_p1.center = ((player_banner.get_rect().width )//2+ 475, (player_banner.get_rect().height )//2+ 600)

# to win text
text_to_win = font2.render("", True, blue)
textRect_to_win = text_p1.get_rect()
textRect_to_win.center = ((to_win_banner.get_rect().width )//2+ 167, (to_win_banner.get_rect().height )//2+ 708)

# run the game
running = True
while running:
    gameDisplay.blit(board_img, (0,0))
    gameDisplay.blit(banner_img, (30,33))
    
    gameDisplay.blit(to_win_banner,(167,708))
    p1_card = player1_deck.draw()
    p2_card = player2_deck.draw()
    p1_card_img = card_creator.create_card(p1_card)
    p2_card_img = card_creator.create_card(p2_card)
    
    #print("Player 1 card: " + str(p1_card))
    #print("Player 2 card: " + str(p2_card))
    #print("Cards to win: " + str(2 + saved_cards.cards_left()))

    gameDisplay.blit(p1_card_img, (75,245))
    gameDisplay.blit(p2_card_img, (475,245))
    gameDisplay.blit(player_banner, (75,600))
    gameDisplay.blit(player_banner, (475,600))

    text = font.render("New round...", True, blue)
    textRect = text.get_rect()
    textRect.center = ((banner_img.get_rect().width )//2+ 30, (banner_img.get_rect().height )//2+ 33)
    gameDisplay.blit(text, textRect)
    text_p1 = font2.render("P1 cards: " +str(player1_deck.cards_total()), True, blue)
    text_p2 = font2.render("P2 cards: " +str(player2_deck.cards_total()), True, blue)
    textRect_p1 = text_p1.get_rect()
    textRect_p1.center = ((player_banner.get_rect().width )//2+ 75, (player_banner.get_rect().height )//2+ 600)
    textRect_p2 = text_p2.get_rect()
    textRect_p2.center = ((player_banner.get_rect().width )//2+ 475, (player_banner.get_rect().height )//2+ 600)
    gameDisplay.blit(text_p1, textRect_p1)
    gameDisplay.blit(text_p2, textRect_p2)

    text_to_win = font2.render("Cards to win: " + str(2 + saved_cards.cards_left()), True, blue)
    textRect_to_win = text_p1.get_rect()
    textRect_to_win.center = ((to_win_banner.get_rect().width )//2+ 167, (to_win_banner.get_rect().height )//2+ 708)
    gameDisplay.blit(text_to_win, textRect_to_win)
    pygame.display.update()
    #input("\nPress Enter to continue...")
    time.sleep(3)
    print_txt = ""
    if card_comp.compare(p1_card,p2_card) < 0:
        print_txt = "Player 2 wins the round"
        player2_deck.discard([p1_card,p2_card])
        player2_deck.discard(saved_cards)
        #print("Player 2 has " + str(player2_deck.cards_total()) + " cards now.")
    elif card_comp.compare(p1_card,p2_card) > 0:
        print_txt = "Player 1 wins the round"
        player1_deck.discard([p1_card,p2_card])
        player1_deck.discard(saved_cards)
        #print("Player 1 has " + str(player1_deck.cards_total()) + " cards now.")
    else:
        print_txt = "WAR!!!!!!!!!"
        saved_cards.insert_cards([p1_card,p2_card,player1_deck.draw(),player2_deck.draw()])
        gameDisplay.blit(to_win_banner,(167,708))
        text_to_win = font2.render("Cards to win: " + str(2 + saved_cards.cards_left()), True, blue)
        textRect_to_win = text_p1.get_rect()
        textRect_to_win.center = ((to_win_banner.get_rect().width )//2+ 167, (to_win_banner.get_rect().height )//2+ 708)
        gameDisplay.blit(text_to_win, textRect_to_win)
    
    gameDisplay.blit(banner_img, (30,33))
    text = font.render(print_txt, True, blue)
    textRect = text.get_rect()
    textRect.center = ((banner_img.get_rect().width )//2+ 30, (banner_img.get_rect().height )//2+ 33)
    gameDisplay.blit(text, textRect)

    pygame.display.update()
    time.sleep(3)
    if player1_deck.cards_total() == 0:
        text = font.render("Player 2 wins!!!!!!", True, blue)
        textRect = text.get_rect()
        textRect.center = ((banner_img.get_rect().width )//2+ 30, (banner_img.get_rect().height )//2+ 33)
        #print("Player 2 wins!!!!!!")
        running = False
        time.sleep(5)
    elif player2_deck.cards_total() == 0:
        text = font.render("Player 1 wins!!!!!!", True, blue)
        textRect = text.get_rect()
        textRect.center = ((banner_img.get_rect().width )//2+ 30, (banner_img.get_rect().height )//2+ 33)
        #print("Player 2 wins!!!!!!")
        running = False
        time.sleep(5)