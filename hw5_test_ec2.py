###############################################
#####  Name: Buyao Lyu                   ######
#####  Uniqname: wqrydqk@umich.edu       ######


import unittest
import hw5_cards_ec2
import random


class TestEc2(unittest.TestCase):

    def test_remove_pairs(self):
        # construct hand_1, instance of Hand
        cards_already_in_hands = \
            [hw5_cards_ec2.Card(0, 1), hw5_cards_ec2.Card(1, 4), hw5_cards_ec2.Card(3, 11), hw5_cards_ec2.Card(3, 12)]
        hand_1 = hw5_cards_ec2.Hand(cards_already_in_hands)

        ## now there are no pairs
        len_before_remove_pairs = len(hand_1.init_card)
        str_list_before = []
        for card in hand_1.init_card:
            str_list_before.append(card.__str__())
        hand_1.remove_pairs()
        len_after_remove_pairs = len(hand_1.init_card)
        str_list_after = []
        for card in hand_1.init_card:
            str_list_after.append(card.__str__())
        self.assertEqual(len_before_remove_pairs, len_after_remove_pairs)  # make sure equal length
        for element in str_list_after:
            self.assertTrue(element in str_list_before)  # make sure str_list_before contains str_list_after
        for element in str_list_after:
            self.assertTrue(element in str_list_before)  # make sure str_list_after contains str_list_before
        # thus the two list are the same

        ## then we add pairs to hand_1
        hand_1.add_card(hw5_cards_ec2.Card(1, 1))
        hand_1.add_card(hw5_cards_ec2.Card(2, 1))  # we have 3 Aces now
        hand_1.add_card(hw5_cards_ec2.Card(0, 12))
        hand_1.add_card(hw5_cards_ec2.Card(1, 12))
        hand_1.add_card(hw5_cards_ec2.Card(2, 12))  # we have 4 Queens now
        hand_1.add_card(hw5_cards_ec2.Card(1, 11))  # we have 2 Jacks now
        # now the cards in hand_1 in 10, with 4 pairs: 4 Q, 2 J and 2 A
        # remove pairs
        random.seed(10)
        hand_1.remove_pairs()
        # now we will only have "4 of Clubs" and one of the Aces in hand
        # test we only have two cards
        self.assertEqual(len(hand_1.init_card), 2)
        # test the two cards are exactly "4 of Club" and one of the Aces
        str_card_in_hand = []
        for card in hand_1.init_card:
            str_card_in_hand.append(card.__str__())
        ace_str_list = ['Ace of Diamonds', 'Ace of Clubs', 'Ace of Hearts']
        random.seed(10)
        ace_st_remains = ace_str_list[random.randint(0,2)]
        self.assertTrue('4 of Clubs' in str_card_in_hand)
        self.assertTrue(ace_st_remains in str_card_in_hand)


    def test_deal(self):
        deck = hw5_cards_ec2.Deck()
        # test (1st situation): number of hands larger than number of cards in deck
        hands_test_1 = deck.deal(400,-1)
        for hand in hands_test_1:
            self.assertEqual(len(hand.init_card), 1)

        # test (2nd situation): the second parameter is set to -1
        hands_test_2 = deck.deal(20,-1)
        self.assertEqual(len(hands_test_2), 20)  # test the number of hands
        self.assertEqual(len(hands_test_2[11].init_card), 3)  # up to 12th hands will get 3 cards
        self.assertEqual(len(hands_test_2[12].init_card), 2)  # from 13th, get 2 cards

        # test (3rd situation): # of hands X # of cards per hand <= 52
        # sub_test_1: empty the deck
        hands_test_3 = deck.deal(4, 13)
        self.assertEqual(len(hands_test_3), 4)  # test number of hands

        self.assertEqual(len(hands_test_3[3].init_card), 13)
        # sub_test_2: do not empty the deck
        hands_test_3 = deck.deal(6, 6)
        self.assertEqual(len(hands_test_3), 6)  # test number of hands
        self.assertEqual(len(hands_test_3[0].init_card), 6)  # test number of cards per hand
        self.assertEqual(len(hands_test_3[1].init_card), 6)
        self.assertEqual(len(hands_test_3[2].init_card), 6)
        self.assertEqual(len(hands_test_3[3].init_card), 6)
        self.assertEqual(len(hands_test_3[4].init_card), 6)
        self.assertEqual(len(hands_test_3[5].init_card), 6)

        # test (4th situation): # of hands X # of cards per hand > 52
        hands_test_4 = deck.deal(3,18)
        self.assertEqual(len(hands_test_4), 3)
        self.assertEqual(len(hands_test_4[0].init_card), 18)  # test number of cards per hand
        self.assertEqual(len(hands_test_4[1].init_card), 17)
        self.assertEqual(len(hands_test_4[2].init_card), 17)


if __name__ == "__main__":
    unittest.main()


