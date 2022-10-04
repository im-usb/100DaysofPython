## RULES OF BLACKJACK

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import art

def compare(comp_score,player_score):
    
    if comp_score > 21 and player_score > 21 or player_score == comp_score:
        return "It's a Draw"

    else:
        if player_score > 21:
            return "Sorry, You Lost."
        elif comp_score > 21:
            return "Amazing! You Win!"
        elif player_score <=21 and player_score > comp_score:
            return "Amazing! You Win!"
        else:
            return "Sorry, You Lost."

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

play_game = 'y'
play_game = input("Do you want to play a game of BlackJack? y or n?: ").lower()

while play_game == 'y':

    #print logo
    print(art.logo)

    player_cards = []
    comp_cards = []

    for i in range(0,2):
        player_cards.append(deal_card())
        comp_cards.append(deal_card())
    
    player_score = sum(player_cards)
    comp_score = sum(comp_cards)

    print(f"Your Cards: {player_cards} Current Score: {player_score}")
    print(f"Computer's Cards: {comp_cards[1]}")
    
    another_card = 'n'
    another_card = input("Type y for Hit, and n for Stand:").lower()

    while another_card == 'y':
        
        player_cards.append(deal_card())
        player_score = sum(player_cards)

        print(f"Your Cards: {player_cards} Current Score: {player_score}")
        print(f"Computer's Cards: {comp_cards[1]}")

        if player_score <= 21:
            another_card = input("Type y for Hit, and n for Stand:").lower()
        else:
            another_card = 'n'

    while comp_score <= 16:
        comp_cards.append(deal_card())
        comp_score = sum(comp_cards)
    
    result = compare(comp_score,player_score)

    print(result)
    #Play Again
    print(f"Computer's Cards: {comp_cards} Player Cards: {player_cards}")
    print(f"Computer's Score: {comp_score} Player Score: {player_score}")
    play_game = input("Do you want to play again? y or n?: ").lower()

print("Thanks :)")
