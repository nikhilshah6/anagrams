"""A bag of letters for finding anagrams.
Associates a cardinality (count) with each character
in the bag.
"""

def normalize(phrase: str) -> list[str]:
    """Normalize word or phrase to the
    sequence of letters we will try to match, discarding
    anything else, such as blanks and apostrophes.
    Return as a list of individual letters.
    """
    normalized = []
    phrase = phrase.lower().replace("'","").replace(" ", "").replace('!','')
    for i in phrase:
        if i.isalpha():
            normalized.append(i.lower())
        
        #else:

            #i = i.lower().replace("'","").replace(" ", "").replace('!','')
           #normalized.append(i)

    return normalized
        

class LetterBag:
    """A bag (also known as a multiset) is
    a map from keys to non-negative integers.
    A LetterBag is a bag of single character
    strings.
    """
    def __init__(self, word=""):
        """Create a LetterBag"""
        self.word = word.strip()
        normal = normalize(self.word)
        self.length = len(normal)  # Counts letters only!
        self.letters = {}

        for i in normal:
            if i not in self.letters:
                self.letters[i] = 1
            else:
                self.letters[i] += 1

    def __len__(self):
        return self.length

    def __str__(self):
        return self.word

    def __repr__(self):
        counts = [f"{ch}:{n}" for ch, n in self.letters.items() if n > 0]
        return f'LetterBag({self.word}/[{", ".join(counts)}])'
    
    def copy(self) -> "LetterBag":
        """Make a copy before mutating."""
        copy_ = LetterBag()
        copy_.word = self.word
        copy_.letters = self.letters.copy()  # Copied to avoid aliasing
        copy_.length = self.length
        return copy_
    
    def contains(self, other: "LetterBag") -> bool:
        """Determine whether enough of each letter in
        other LetterBag are contained in this LetterBag.
        """

        '''for letter in other.letters:
            if letter not in self.letters:
                return False
            
            if self.letters[letter] < other.letters[letter]:
                return False
            
        return True'''
        
        copy_other_letters = other.letters.copy()
        for i in self.letters:
            #print(copy_other_letters)
            if i in copy_other_letters:
                copy_other_letters[i] -= self.letters[i]

                if copy_other_letters[i] <= 0:
                    copy_other_letters.pop(i, None)

        if copy_other_letters == {}:
            return True
        else:
            return False
        


    def take(self, other: "LetterBag") -> "LetterBag":
       

       '''bag = self.copy()

       assert bag.contains(other)

       for letter, count in other.letters.items():
           
           bag.letters[letter] -= count

       bag.length -= other.length
       
       return bag'''



       bag = self.copy()
       for i in self.letters:
            if i in other.letters:
                assert self.letters[i] >= other.letters[i]
                bag.letters[i] -= other.letters[i]

                if bag.letters[i] <= 0:
                    bag.letters.pop(i, None)
                
        #bag.length = len(normalize(bag.word))
       bag.length = sum(bag.letters.values())
       return bag
    
    
    