############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

import random
from art import logo
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def compute_totals(hand):
    total = 0
    for card in hand:
        total += card
    return total


def print_totals(player_hand, computer_hand, player_total):
    print(f"Your cards: {player_hand}, current score: {player_total}")
    print(f"Computer's first card: {computer_hand[0]}")


def blackjack():
    wanna_play = (
        input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    ).lower()

    if wanna_play == "y":
        os.system("clear")
        print(logo)

        player_hand = random.sample(cards, 2)
        computer_hand = random.sample(cards, 2)

        player_total = compute_totals(player_hand)

        print_totals(player_hand, computer_hand, player_total)

        player_continue = True

        if player_total == 21:
            player_continue = False
            print("Win with a Blackjack 😎")

        while player_continue:
            if (
                (input("Type 'y' to get another card, type 'n' to pass: ")).lower()
            ) == "y":
                player_hand.extend(random.sample(cards, 1))

                player_total = compute_totals(player_hand)
                if player_total > 21 and player_hand[-1] == 11:
                    player_total -= 10
                    player_hand[-1] = 1
                print_totals(player_hand, computer_hand, player_total)
                if player_total > 21:
                    player_continue = False
                    computer_total = compute_totals(computer_hand)
                    while computer_total <= 16:
                        computer_hand.extend(random.sample(cards, 1))
                        computer_total = compute_totals(computer_hand)
                        if computer_total > 21 and computer_hand[-1] == 11:
                            computer_total -= 10
                            computer_hand[-1] = 1
                    print(
                        f"Your final hand: {player_hand}, final score: {player_total}"
                    )
                    print(
                        f"Computer's final hand: {computer_hand}, final score: {computer_total}"
                    )
                    print("You went over. You lose 😤")
                    blackjack()

            else:
                player_continue = False
                print(f"Your final hand: {player_hand}, final score: {player_total}")
                computer_total = compute_totals(computer_hand)
                while computer_total <= 16:
                    computer_hand.extend(random.sample(cards, 1))
                    computer_total = compute_totals(computer_hand)
                    if computer_total > 21 and computer_hand[-1] == 11:
                        computer_total -= 10
                        computer_hand[-1] = 1
                print(
                    f"Computer's final hand: {computer_hand}, final score: {computer_total}"
                )
                if computer_total > 21:
                    print("Opponent went over. You win 😁")
                elif player_total == computer_total:
                    print("Draw 🙃")
                elif player_total > computer_total:
                    print("You win 😃")

        blackjack()


blackjack()
