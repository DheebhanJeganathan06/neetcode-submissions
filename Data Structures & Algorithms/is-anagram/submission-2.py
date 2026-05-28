class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_dict = {}
        for letter in s:
            letter_dict[letter] = letter_dict.get(letter, 0) + 1
        for letter in t:
            if not (letter in letter_dict):
                return False
            letter_dict[letter] = letter_dict.get(letter) - 1

        for letter in letter_dict:
            if not (letter_dict.get(letter) == 0 ):
                return False
        return True

        