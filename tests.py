#!/usr/bin/env python

import game
import unittest
from collections import Counter

class TestGame(unittest.TestCase):

    def setUp(self):
        self.g = game.Game([])

    def test_cmpdices(self):
        cases = []
        cases.append(('1223','6666', -1))
        cases.append(('1116','5555', 1))
        cases.append(('1116','1116', 0))
        cases.append(('111111','122346', -1))
        cases.append(('111112','111111', 1))
        cases.append(('111126','111112', 1))
        cases.append(('111226','111126', 1))
        cases.append(('111266','111226', 1))
        cases.append(('112266','111266', 1))
        cases.append(('11444','23356', -1))
        for a, b, c in cases:
            self.assertEqual(c, self.g.cmp_subs(a,b))
            # print a, b, 'OK' if c==g.cmp_subs(a,b) else ':C', g.cmp_subs(a,b), c

    def test_is_in_dices(self):
        cases = []
        cases.append(('1223','6666', True))
        cases.append(('1116','5555', False))
        cases.append(('1116','1116', True))
        cases.append(('111111','122346', True))
        cases.append(('111112','111111', False))
        cases.append(('111126','111112', False))
        cases.append(('111226','111126', False))
        cases.append(('111266','111226', False))
        cases.append(('112266','111266', False))
        cases.append(('11444','23356', False))
        for a, b,c in cases: 
            self.assertEqual(c, self.g.is_in_dices(a,b))

    def test_sub_valid(self):
        cases = []
        cases.append(('11124', True))
        cases.append(('11421', False))
        cases.append(('11137', False))
        cases.append(('11424', False))
        for a, b in cases: 
            # is valid checks if len(submission)==number of dices
            # so lets fake it
            self.g.k = [len(a)]
            self.assertEqual(b, self.g.is_valid(a))


    def test_roll_dices(self):
        n = 600000
        eps = 0.01
        cnt = Counter(self.g.gen_dices(n)).values()
        self.assertEqual(True, all(map(lambda x: 1/6. - eps < x/float(n) < 1/6. + eps, cnt)))


if __name__ == '__main__':
    unittest.main()