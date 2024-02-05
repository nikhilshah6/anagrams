"""Test cases for anagram.py"""

import unittest
import anagram
#from letter_bag
import letter_bag
import word_heuristic

class Test_Read(unittest.TestCase):
    """Test reading and sorting the word list"""

    def test_read(self):
        """Just reading the word list"""
        with open("data/cs_sample.txt") as f:
            words = anagram.read_word_list(f)
        expect = ["transform", "mop", "income", "secret",
                  "cup", "use", "eccentric"]
        self.assertListEqual(words, expect)

class Test_Anagram_Search(unittest.TestCase):
    """Tests for the anagram search per se"""
    
    def test_search_simple(self):
        """Search should automatically ignore non-letter characters"""
        with open("data/cs_sample.txt") as f:
            words = anagram.read_word_list(f)
        candidates = [letter_bag.LetterBag(word) for word in words]
        target = letter_bag.LetterBag("Computer science!")
        anagrams = anagram.search(target, candidates)
        self.assertListEqual(anagrams, ["mop use eccentric", "income secret cup"])


    def test_search_sorted(self):
        """Without constraints on the search"""
        with open("data/cs_sample.txt") as f:
            words = anagram.read_word_list(f)
        words.sort(key=word_heuristic.score, reverse=True)
        candidates = [letter_bag.LetterBag(word) for word in words]
        
        target = letter_bag.LetterBag("computer science")
        anagrams = anagram.search(target, candidates)
        self.assertListEqual(anagrams, ["eccentric mop use", "income secret cup"])
if __name__ == "__main__":
    unittest.main()