class Solution:
    def isPalindrome(self, s: str) -> bool:
        resultstring = ""

        for char in s:
            if char.isalnum():
                resultstring += char.lower()
        
        return resultstring == resultstring[::-1]