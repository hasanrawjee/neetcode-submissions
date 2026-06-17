class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        charCount = {}

        for r in range(len(s)):
            charCount[s[r]] = 1 + charCount.get(s[r], 0)

            while (r - l + 1) - max(charCount.values()) > k:
                charCount[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res