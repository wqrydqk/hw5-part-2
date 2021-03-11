###############################################
#####  Name: Buyao Lyu                   ######
#####  Uniqname: wqrydqk@umich.edu       ######


import unittest
import hw5_cards_ec1


class TestHand(unittest.TestCase):

    def test_construct_Hand(self):
        cards_already_in_hands = \
            [hw5_cards_ec1.Card(0, 1), hw5_cards_ec1.Card(1, 4), hw5_cards_ec1.Card(3, 11), hw5_cards_ec1.Card(3, 12)]
        hand_1 = hw5_cards_ec1.Hand(cards_already_in_hands)
        self.assertIsInstance(hand_1, hw5_cards_ec1.Hand)
        self.assertIsInstance(hand_1.init_card, list)
        self.assertEqual(hand_1.init_card[0].__str__(), "Ace of Diamonds")
        self.assertEqual(hand_1.init_card[1].__str__(), "4 of Clubs")
        self.assertEqual(hand_1.init_card[2].__str__(), "Jack of Spades")
        self.assertEqual(hand_1.init_card[3].__str__(), "Queen of Spades")

    def testAddAndRemove(self):
        cards_already_in_hands = \
            [hw5_cards_ec1.Card(0, 1), hw5_cards_ec1.Card(1, 4), hw5_cards_ec1.Card(3, 11), hw5_cards_ec1.Card(3, 12)]
        hand_1 = hw5_cards_ec1.Hand(cards_already_in_hands)

        # test a card already in hand
        card_in = hand_1.init_card[2]
        initial_length = len(hand_1.init_card)
        hand_1.add_card(card_in)
        length_after_add = len(hand_1.init_card)
        self.assertEqual(initial_length, length_after_add)
        card_to_remove = hand_1.remove_card(card_in)
        self.assertEqual(card_to_remove.__str__(), "Jack of Spades")
        self.assertEqual(len(hand_1.init_card), length_after_add - 1)

        # test a card not in hand
        card_not_in = card_in  # we've already removed it, so not in
        response = hand_1.remove_card(card_not_in)
        self.assertEqual(response, None)
        current_length = len(hand_1.init_card)
        hand_1.add_card(card_not_in)
        self.assertEqual(len(hand_1.init_card), current_length + 1)

    def test_draw(self):
        # construct hand_1, instance of Hand
        cards_already_in_hands = \
            [hw5_cards_ec1.Card(0, 1), hw5_cards_ec1.Card(1, 4), hw5_cards_ec1.Card(3, 11), hw5_cards_ec1.Card(3, 12)]
        hand_1 = hw5_cards_ec1.Hand(cards_already_in_hands)

        # construct deck, instance of Deck
        deck = hw5_cards_ec1.Deck()

        # eliminate cards already in hand_1 from deck
        deck_existing_card_str = []
        for deck_card in deck.cards:
            deck_existing_card_str.append(deck_card.__str__())
        hand_existing_card_str = []
        for hand_card in hand_1.init_card:
            hand_existing_card_str.append(hand_card.__str__())
        deck_str_to_use = []
        for deck_card_str in deck_existing_card_str:
            if deck_card_str not in hand_existing_card_str:
                deck_str_to_use.append(deck_card_str)
        deck_to_use = []
        for deck_card in deck.cards:
            if deck_card.__str__() in deck_str_to_use:
                deck_to_use.append(deck_card)
        deck.cards = deck_to_use

        # test starts
        current_len_hand_cards = len(hand_1.init_card)
        current_len_deck_cards = len(deck.cards)

        # make sure they compensate for each other
        self.assertEqual(current_len_hand_cards + current_len_deck_cards, 52)
        hand_1.draw(deck)
        after_len_hand_cards = len(hand_1.init_card)
        after_len_deck_cards = len(deck.cards)
        self.assertEqual(after_len_hand_cards, current_len_hand_cards + 1)
        self.assertEqual(after_len_deck_cards, current_len_deck_cards - 1)


if __name__ == "__main__":
    unittest.main()
