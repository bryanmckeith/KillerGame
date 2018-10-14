#!/usr/bin/python
# -*- coding: latin-1 -*-

import unittest
from getcode import get_code
from link import assign_players_a_target

class killer_game_test(unittest.TestCase):

    # Set up self for our needs :
    def setUp(self):
        self.string_list = ["My Name", \
                            "My FirstName", \
                            "my_Pseudo_123!", \
                            "+33 01 23 45 67 89"]
        self.people = ["Bruno", "Aurelie", "Alex", "Loic", "Geraud", "Cyril", \
                       "Cedric", "Justine", "Teddy", "Sylvain"]

    def test_get_code(self):
        """ Make sure 2 codes are different although made of same strings """
        i = 0
        while i < 10:                
            first_code = get_code(self.string_list[0], \
                     self.string_list[1], \
                     self.string_list[2], \
                     self.string_list[3])

            second_code = get_code(self.string_list[0], \
                     self.string_list[1], \
                     self.string_list[2], \
                     self.string_list[3])

            self.assertNotEqual(first_code, second_code)
            i += 1        

    def test_assign_players_a_target(self):
        """ Make sure someone can NOT be a target for him/herself """
        i = 0
        while i < 10:  
            targets = assign_players_a_target(self.people)
            for target in targets.items() :
                self.assertNotEqual(target[0], target[1])
            i += 1