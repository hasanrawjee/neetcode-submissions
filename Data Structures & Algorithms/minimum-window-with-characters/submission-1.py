class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # If t is empty, return an empty string
        if t == "": return ""
        # Initialize 2 hashmaps, one for t and one for the window
        countT, window = {}, {}
        # Iterate through t and store the count in the hashmap
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        # Initialize l, have, need, res, & resLen variables
        l = 0
        have = 0
        need = len(countT)
        res = [-1, -1]
        resLen = float("infinity")
        # For r in the range len(s), store the count in window hashmap
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            # If s[r] in countT hashmap & is equal in both hashmaps, increment have
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            # While have is equal to need, if the window length is less than resLen
            # then update res to [l, r] & reslen to the window size
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # To shorten the window to the minimum, remove the left char from window
                window[s[l]] -= 1
                # If s[l] in countT & window for that char is less than countT for that char, decrement have
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                # Increment l.
                l += 1
        # Finally set l, r to res.
        l, r = res
        # Return s[l:r+1] if reslen is not infinity, else return empty string
        return s[l:r+1] if resLen != float("infinity") else ""