###############################################
#####  Name: Buyao Lyu                   ######
#####  Uniqname: wqrydqk@umich.edu       ######


import random
import unittest

VERSION = 0.01


class Card:
    '''a standard playing card
    cards will have a suit and a rank
    Class Attributes
    ----------------
    suit_names: list
        the four suit names in order
        0:Diamonds, 1:Clubs, 2: Hearts, 3: Spades

    faces: dict
        maps face cards' rank name
        1:Ace, 11:Jack, 12:Queen,  13:King
    Instance Attributes
    -------------------
    suit: int
        the numerical index into the suit_names list
    suit_name: string
        the name of the card's suit
    rank: int
        the numerical rank of the card
    rank_name: string
        the name of the card's rank (e.g., "King" or "3")
    '''
    suit_names = ["Diamonds", "Clubs", "Hearts", "Spades"]
    faces = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.suit_name = Card.suit_names[self.suit]

        self.rank = rank
        if self.rank in Card.faces:
            self.rank_name = Card.faces[self.rank]
        else:
            self.rank_name = str(self.rank)

    def __str__(self):
        return f"{self.rank_name} of {self.suit_name}"


class Deck:
    '''a deck of Cards
    Instance Attributes
    -------------------
    cards: list
        the list of Cards currently in the Deck. Initialized to contain
        all 52 cards in a standard deck
    '''

    def __init__(self):

        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)  # appends in a sorted order

    def deal_card(self, i=-1):
        '''remove a card from the Deck
        Parameters
        -------------------
        i: int (optional)
            the index of the ard to remove. Default (-1) will remove the "top" card

        Returns
        -------
        Card
            the Card that was removed
        '''
        return self.cards.pop(i)

    def shuffle(self):
        '''shuffles (randomizes the order) of the Cards
        self.cards is modified in place
        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        random.shuffle(self.cards)

    def replace_card(self, card):
        card_strs = []  # forming an empty list
        for c in self.cards:  # each card in self.cards (the initial list)
            card_strs.append(c.__str__())  # appends the string that represents that card to the empty list
        if card.__str__() not in card_strs:  # if the string representing this card is not in the list already
            self.cards.append(card)  # append it to the list

    def sort_cards(self):
        '''returns the Deck to its original order

        Cards will be in the same order as when Deck was constructed.
        self.cards is modified in place.
        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def deal_hand(self, hand_size):
        '''removes and returns hand_size cards from the Deck

        self.cards is modified in place. Deck size will be reduced
        by hand_size
        Parameters
        -------------------
        hand_size: int
            the number of cards to deal
        Returns
        -------
        list
            the top hand_size cards from the Deck
        '''
        hand_cards = []
        for i in range(hand_size):
            hand_cards.append(self.deal_card())
        return hand_cards

    def deal(self, num_hands, num_cards_per_hand=-1):
        ''' deal the deck and return a list of hands

        deal the deck with the parameters num_hands and num_cards_per_hands
        if the second parameter is -1, then the deck should be emptied to
        generate the list of hands; else, the list of hands will be generated
        by analyzing the two parameters

        Parameters
        ----------
        num_hands: int
            the number of hands to divide the deck
        num_cards_per_hand: int
            the number of cards per hand

        Returns
        -------
        list
            a list in which every element is an instance of Hand
        '''

        self.shuffle()
        hands_list = []
        # if num_hands larger than total cards in deck
        # assign 52 hands one card per hand and ignore the remaining hands
        if num_hands > len(self.cards):
            # print('+---------------------------------------------+')
            # print('# of hands larger than total # of cards!')
            # print('somebody will not have cards!')
            for card in self.cards:
                temp_list = []
                temp_list.append(card)
                temp_hand = Hand(temp_list)
                hands_list.append(temp_hand)
            return hands_list

        else:
            # if num_hands <= 52 but num_cards_per_hand == -1
            # then we will empty the deck
            if num_cards_per_hand == -1:
                # print('+----------------------------------------------+')
                # print('since cards per hand is -1, card in deck will be used up!')
                original_list = self.cards
                card_per_hand = len(self.cards)//num_hands
                cards_left = len(self.cards) - card_per_hand * num_hands
                threshold_for_more_and_less = cards_left * (card_per_hand + 1)
                for i in range(0, threshold_for_more_and_less, card_per_hand+1):
                    hands_for_more_cards = original_list[i:i+card_per_hand+1]
                    temp_more_card_hand = Hand(hands_for_more_cards)
                    hands_list.append(temp_more_card_hand)

                less_cards_list = original_list[threshold_for_more_and_less:]
                for i in range(0, len(less_cards_list), card_per_hand):
                    hands_for_less_cards = less_cards_list[i:i+card_per_hand]
                    temp_less_card_hand = Hand(hands_for_less_cards)
                    hands_list.append(temp_less_card_hand)
                return hands_list

            else:
                # if num_cards_per_hand != -1, num_hands <= 52 and
                # the multiplication smaller than 52
                # assign each hand same amount of cards
                if num_hands * num_cards_per_hand <= len(self.cards):
                    # print('+----------------------------------------------+')
                    # print('everyone will be guranteed to have equal # of cards!')
                    original_list = self.cards
                    threshold_for_card = num_hands * num_cards_per_hand
                    for i in range(0, threshold_for_card, num_cards_per_hand):
                        hands_for_more_cards = original_list[i:i + num_cards_per_hand]
                        temp_more_card_hand = Hand(hands_for_more_cards)
                        hands_list.append(temp_more_card_hand)
                    return hands_list

                else:
                    # if num_cards_per_hand != -1, num_hands <= 52 but
                    # the multiplication larger than 52
                    # empty the deck, like the case num_cards_per_hand == -1
                    # print('+----------------------------------------------+')
                    # print('cards will be used up and every hand may have different # of cards!')
                    original_list = self.cards
                    card_per_hand = len(self.cards) // num_hands
                    cards_left = len(self.cards) - card_per_hand * num_hands
                    threshold_for_more_and_less = cards_left * (card_per_hand + 1)
                    for i in range(0, threshold_for_more_and_less, card_per_hand + 1):
                        hands_for_more_cards = original_list[i:i + card_per_hand + 1]
                        temp_more_card_hand = Hand(hands_for_more_cards)
                        hands_list.append(temp_more_card_hand)

                    less_cards_list = original_list[threshold_for_more_and_less:]
                    for i in range(0, len(less_cards_list), card_per_hand):
                        hands_for_less_cards = less_cards_list[i:i + card_per_hand]
                        temp_less_card_hand = Hand(hands_for_less_cards)
                        hands_list.append(temp_less_card_hand)
                    return hands_list


class Hand:
    '''a hand for playing card

    Class Attributes
    ----------------
    None

    Instance Attributes
    -------------------
    init_card: list
        a list of cards
    '''

    def __init__(self, init_cards):
        self.init_card = init_cards

    def add_card(self, card):
        '''add a card
        add a card to the hand
        silently fails if the card is already in the hand

        Parameters
        ----------
        card: instance
            a card to add

        Returns
        -------
        None
        '''

        card_strs = []
        for c in self.init_card:
            card_strs.append(c.__str__())
        if card.__str__() not in card_strs:
            self.init_card.append(card)

    def remove_card(self, card):
        '''remove a card from hand

        Parameters
        ----------
        card: instance
            a card to remove

        Returns
        -------
        the card, or None if the card was not in the hand
        '''

        card_strs = []
        for c in self.init_card:
            card_strs.append(c.__str__())
        if card.__str__() in card_strs:
            card_to_remove_index = card_strs.index(card.__str__())
            card_to_remove = self.init_card.pop(card_to_remove_index)
            return card_to_remove
        else:
            return None

    # def draw(self, deck):
    #     '''draw a card
    #     draw a card from a deck and add it to the hand
    #     side effect: the deck will be deplete by one card
    #
    #     Parameters
    #     ----------
    #     deck: instance
    #         a deck from which to draw
    #
    #     Returns
    #     -------
    #     None
    #     '''
    #     deck_existing_card_str = []
    #     for deck_card in deck.cards:
    #         deck_existing_card_str.append(deck_card.__str__())
    #     hand_existing_card_str = []
    #     for hand_card in self.init_card:
    #         hand_existing_card_str.append(hand_card.__str__())
    #     deck_str_to_use = []
    #     for deck_card_str in deck_existing_card_str:
    #         if deck_card_str not in hand_existing_card_str:
    #             deck_str_to_use.append(deck_card_str)
    #     deck_to_use = []
    #     for deck_card in deck.cards:
    #         if deck_card.__str__() in deck_str_to_use:
    #             deck_to_use.append(deck_card)
    #     deck.cards = deck_to_use
    #
    #     card_from_deck = deck.cards.pop(-1)
    #     card_to_hand = card_from_deck
    #     self.init_card.append(card_to_hand)

    def draw(self, deck):
        '''draw a card
        draw a card from a deck and add it to the hand
        side effect: the deck will be deplete by one card

        Parameters
        ----------
        deck: instance
            a deck from which to draw

        Returns
        -------
        None
        '''
        card_from_deck = deck.cards.pop(-1)
        self.init_card.append(card_from_deck)

    def remove_pairs(self):
        ''' find all of the pairs in a Hand instance and remove all of them

        firstly find out all of the pairs, then remove them
        note that if there are three of a kind, randomly remove two of them,
        if there are four of a kind, remove all of them

        Paramters
        ---------
        None

        Returns
        -------
        None
        '''

        dict_record_times = {}
        for num in range(1,14):
            list_for_the_key = []
            for card in self.init_card:
                if card.rank == num:
                    list_for_the_key.append(card)
                    dict_record_times[num] = list_for_the_key
        self.init_card = []
        for key in dict_record_times.keys():
            num_of_same_rank = len(dict_record_times[key])
            if num_of_same_rank == 1:
                self.init_card.append(dict_record_times[key][0])
            if num_of_same_rank == 3:
                self.init_card.append(dict_record_times[key][random.randint(0,2)])


def print_hand(hand):
    '''prints a hand in a compact form

    Parameters
    -------------------
    hand: list
        list of Cards to print
    Returns
    -------
    none
    '''
    hand_str = '/ '
    for c in hand:
        s = c.suit_name[0]
        r = c.rank_name[0]
        hand_str += r + "of" + s + ' / '
    print(hand_str)
