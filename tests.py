import unittest
from algorithms import brute_force, kmp, \
    rabin_karp_algorithm, boyer_moore_algorithm, kmpm

given = ['A9F7JVH-0LR7TKH', 'G04;VOQNVA8TRJ7H09RT`',
         '*{7FY/?)?{,>:SZH6O3A', 'C9?S,G$@4D7YSIC|@?Q~', '',
         'AAAAA', 'ABCDAAAAABCD', 10]

unknown = ['A', 10]


class TestFirstOccurrence(unittest.TestCase):

    def testBF(self):
        self.assertEqual(0, brute_force(given[0], unknown[0]))

    def testKMP(self):
        self.assertEqual(0, kmp(given[0], unknown[0]))

    def testKMPM(self):
        self.assertEqual([0], kmpm(given[0], unknown[0]))

    def testBM(self):
        self.assertEqual(0, boyer_moore_algorithm(given[0], unknown[0]))

    def testRK(self):
        self.assertEqual(0, rabin_karp_algorithm(given[0], unknown[0]))


class TestEnteringInTheMiddle(unittest.TestCase):

    def testBF(self):
        self.assertEqual(9, brute_force(given[1], unknown[0]))

    def testKMP(self):
        self.assertEqual(9, kmp(given[1], unknown[0]))

    def testKMPM(self):
        self.assertEqual([9], kmpm(given[1], unknown[0]))

    def testBM(self):
        self.assertEqual(9, boyer_moore_algorithm(given[1], unknown[0]))

    def testRK(self):
        self.assertEqual(9, rabin_karp_algorithm(given[1], unknown[0]))


class TestLastOccurrence(unittest.TestCase):

    def testBF(self):
        self.assertEqual(19, brute_force(given[2], unknown[0]))

    def testKMP(self):
        self.assertEqual(19, kmp(given[2], unknown[0]))

    def testKMPM(self):
        self.assertEqual([19], kmpm(given[2], unknown[0]))

    def testBM(self):
        self.assertEqual(19, boyer_moore_algorithm(given[2], unknown[0]))

    def testRK(self):
        self.assertEqual(19, rabin_karp_algorithm(given[2], unknown[0]))


class TestNoOccurrence(unittest.TestCase):

    def testBF(self):
        self.assertEqual(-1, brute_force(given[3], unknown[0]))

    def testKMP(self):
        self.assertEqual(-1, kmp(given[3], unknown[0]))

    def testKMPM(self):
        self.assertEqual([], kmpm(given[3], unknown[0]))

    def testBM(self):
        self.assertEqual(-1, boyer_moore_algorithm(given[3], unknown[0]))

    def testRK(self):
        self.assertEqual(-1, rabin_karp_algorithm(given[3], unknown[0]))


class TestEmptyString(unittest.TestCase):

    def testBF(self):
        self.assertEqual(-1, brute_force(given[4], unknown[0]))

    def testKMP(self):
        self.assertEqual(-1, kmp(given[4], unknown[0]))

    def testKMPM(self):
        self.assertEqual(None, kmpm(given[4], unknown[0]))

    def testBM(self):
        self.assertEqual(-1, boyer_moore_algorithm(given[4], unknown[0]))

    def testRK(self):
        self.assertEqual(-1, rabin_karp_algorithm(given[4], unknown[0]))


class TestManyOccurrence(unittest.TestCase):

    def firstTestKMPM(self):
        self.assertEqual([0, 1, 2, 3, 4], kmpm(given[5], unknown[0]))

    def secondTestKMPM(self):
        self.assertEqual([0, 4, 5, 6, 7, 8], kmpm(given[6], unknown[0]))


class TestIntText(unittest.TestCase):

    def testBF(self):
        self.assertRaises(TypeError, brute_force, given[7], unknown[0])

    def testKMP(self):
        self.assertRaises(TypeError, kmp, given[7], unknown[0])

    def testKMPM(self):
        self.assertRaises(TypeError, kmpm, given[7], unknown[0])

    def testRK(self):
        self.assertRaises(TypeError, rabin_karp_algorithm,
                          given[7], unknown[0])


class TestIntPatterns(unittest.TestCase):
    def testBF(self):
        self.assertRaises(TypeError, brute_force, given[0], unknown[1])

    def testKMP(self):
        self.assertRaises(TypeError, kmp, given[0], unknown[1])

    def testKMPM(self):
        self.assertRaises(TypeError, kmpm, given[0], unknown[1])

    def testRK(self):
        self.assertRaises(TypeError, rabin_karp_algorithm,
                          given[0], unknown[1])
