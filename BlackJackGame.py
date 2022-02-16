import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playing = True

start_game = input("Do you want to play a game of blackjack? (Y/N)\n").upper()
if start_game == "N":
    drawing_cards = False

while playing:
    drawing_cards = True

    # makes a seperate array of cards that can be changed
    dealt_cards = cards
    dealer_cards = []
    player_cards = []

    # adds two cards to dealer deck
    card1 = random.choice(dealt_cards)
    card2 = random.choice(dealt_cards)
    dealer_cards.append(card1)
    dealer_cards.append(card2)

    # add two cards to user deck
    card1_user = random.choice(dealt_cards)
    card2_user = random.choice(dealt_cards)
    player_cards.append(card1_user)
    player_cards.append(card2_user)



    while drawing_cards:
        # shows the user one of the dealer cards and both of
        # their cards, then asks if they wish to continue.
        if len(dealer_cards) < 3:
            continue_draw = input(
                f"The dealer has a {card1}.  Your cards are {player_cards}, and their sum is {sum(player_cards)}."
                f" \ndo you wish to continue? (Y/N)\n").upper()
        else:
            continue_draw = input(
                f"The dealer has a {dealer_cards}.  Your cards are {player_cards}, and their sum is {sum(player_cards)}."
                f" \ndo you wish to continue? (Y/N)\n").upper()
        if continue_draw == "N":
            drawing_cards = False

        # adds a new card to the dealers hand
        while sum(dealer_cards) < 21 and sum(dealer_cards) < sum(player_cards):
            print("the dealer chose to take a card")
            dealer_card = random.choice(dealt_cards)
            dealer_cards.append(dealer_card)

        # adds a new card to the player's hand
        if drawing_cards:
            new_card = random.choice(dealt_cards)
            player_cards.append(new_card)

        # auto lose conditions.
        if sum(player_cards) > 21:
            drawing_cards = False
            print(f"Your cards add up to be {sum(player_cards)}. You have lost.")
        if sum(dealer_cards) > 21:
            drawing_cards = False
            print(f"You have automatically won, as the dealer's cards add up to be {sum(dealer_cards)}")

    print(f"The game has ended.  Your cards' sum is {sum(player_cards)}, "
          f"\nand the dealer's cards' sum is {sum(dealer_cards)}.")
    if sum(dealer_cards) <= 21 and sum(dealer_cards) > sum(player_cards):
        print("The dealer's cards are greater than the sum of yours. Sorry, but you lost.")
    elif sum(player_cards) <= 21 and sum(player_cards) > sum(dealer_cards):
        print("Your cards' sum is greater than the dealer's cards' sum! you won!")

    print(f"Dealers cards: {dealer_cards} Player cards: {player_cards}")
    keep_playing = input("Do you wish to play again? (Y/N)\n").upper()
    if keep_playing == "N":
        playing = False

