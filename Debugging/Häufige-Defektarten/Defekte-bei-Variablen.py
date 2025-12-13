import random

def get_card(deck: list) -> tuple:
    """Randomly remove a single card from the deck and return it.
    Assumes the deck is not empty.

    deck: A deck as described above.

    Returns: a single card, which is a tuple with
    two elements, the rank and the suit.
    """

    index = int(len(deck) * random.random())
    new_card = deck[index]
    del deck[index]
    return new_card

def draw_card(name: str, deck: list, player_hand: dict) -> None:
    """Draw a new card from the deck and add it to
    hand. If the hand now holds the rank in all four
    suits, then remove them from the hand.

    name: A string with the name of player_hand, used
          only for display purposes.
    deck: A deck as described above.
    hand: A hand dictionary as described above.

    Returns: None.
    """
    if len(deck) > 0:  # guard against an empty deck
        new_card = get_card(deck)
        card_rank, card_suit = new_card[0], new_card[1]

        if card_rank in player_hand:
            # append this suit to the list
            player_hand[card_rank].append(card_suit)
            if len(player_hand[card_rank]) == 4:
                print(f"{name} lays down {card_rank}")
                del player_hand[card_rank]
        else:
            # first of this suit, create a list with one element
            player_hand[card_rank] = [card_suit]
	

def check_card(
    name_of_hand: str, hand_of_player: dict, rank_of_card: str, hand_of_opponent: dict
) -> bool:
    """Check if opponent_hand contains any cards of the
    specified rank, if it does, transfer them to player_hand.

    hand_name: A string with the name of player_hand
    player_hand: A hand dictionary, as described above
    card_rank: A string with the name of a
               card rank ("2" through "10", "J", "Q", "K, or "A")
    opponent_hand: A hand dictionary, as described above

    Returns: True if a card is transferred, False otherwise
    """
    if rank_of_card not in hand_of_opponent:
        return False
    
    transfer_cards: list = hand_of_opponent[rank_of_card]
    # transfer_cards is a list!
    #del hand_of_opponent[rank_of_card]
    if rank_of_card in hand_of_player:
        hand_of_player[rank_of_card].extend(transfer_cards)
    else:  # shouldn't happen, but handle it
        hand_of_player[rank_of_card] = transfer_cards

    if len(hand_of_player[rank_of_card]) == 4:
        print(f"{name_of_hand} lays down {rank_of_card}")
        del hand_of_player[rank_of_card]

    return True


def do_turn(
    hand_name: str, deck: list[tuple], player_hand: dict, opponent_hand: dict
) -> None:
    """Play one turn of 'Go Fish'. A rank in player_hand is chosen,
    and if any cards of that rank exist in opponent_hand, they are transferred.
    This continues until no cards are transferred,
    at which point a new card is drawn from the deck into player_hand.

    hand_name: A string with the name of player_hand.
    deck: The current deck, a list of two-element tuples of the form (rank, suit).
    player_hand: A hand dictionary.
    opponent_hand: A hand dictionary.

    Returns: None.
    """

    """ Loop unless the player_hand is empty. Normally this loop exits via the break statement,
        when check_card() returns false meaning a card was not transferred.
    """

    while len(player_hand):
        """Pick a random index within the current hand..."""
        index = int(len(player_hand) * random.random())

        """ ...and use the rank of the card at that index as the one to ask for.
        """
        rank_to_check = list(player_hand.keys())[index]
        found = check_card(hand_name, opponent_hand, rank_to_check, player_hand)

        if not found:
            break

    # no transfer, so "go fish"
    draw_card(hand_name, deck, player_hand)


ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["spades", "hearts", "diamonds", "clubs"]


def play_go_fish() -> None:
    """Initialization and loop of the game 'Go Fish'."""

    deck: list[tuple] = []
    hand1 = {}
    hand2 = {}

    for i in range(52):
        deck.append((ranks[i % 13], suits[i % 4]))

    for i in range(7):
        draw_card("HAND1", deck, hand1)
        draw_card("HAND2", deck, hand2)

    while True:
        do_turn("HAND1", deck, hand1, hand2)
        do_turn("HAND2", deck, hand2, hand1)

        if len(hand1) == 0 and len(hand2) == 0:
            break