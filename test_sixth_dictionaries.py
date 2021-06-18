import unittest

class test_dictionariers(unittest.TestCase):

    def test_adjectives(self):
        test = open("adjectives.txt").read()
        self.assertIn("abandoned", test)
        self.assertIn("flat", test)
        self.assertIn("visible", test)
        self.assertIn("zigzag", test)

    def test_adverbs(self):
        test = open("adverbs.txt").read()
        self.assertIn("abnormally", test)
        self.assertIn("deeply", test)
        self.assertIn("patiently", test)
        self.assertIn("zestily", test)

    def test_nouns(self):
        test = open("nouns.txt").read()
        self.assertIn("people", test)
        self.assertIn("bath", test)
        self.assertIn("strength", test)
        self.assertIn("yesterday", test)

    def test_verbs(self):
        test = open("verbs.txt").read()
        self.assertIn("abide", test)
        self.assertIn("cheer", test)
        self.assertIn("owe", test)
        self.assertIn("zoom", test)








if __name__ == '__main__':
    unittest.main()