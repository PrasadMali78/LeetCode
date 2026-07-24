class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        # If all letters are uppercase
        if word == word.upper():
            return True

        # If all letters are lowercase
        if word == word.lower():
            return True

        # If only the first letter is uppercase
        if word[0].isupper() and word[1:] == word[1:].lower():
            return True

        return False