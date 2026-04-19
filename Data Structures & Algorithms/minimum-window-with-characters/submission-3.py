class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        problem statement: shortest substring of s, such that every character in t, including
        duplicates, is present in the substring

        brute force: count frequency of all chars in t, compute every possible substring in s,
        and store the smallest substring that has matching frequency to chars in t

        optimal: use sliding window, store frequency of all chars in window.

        while window doesn't hv needed chars in freq, increment right pointer
            

        once it does, increment left, checking if it still meets criteria
        store minimum length of valid substring

        substring = sliding window!
        '''

        if t == "":
            return ""

        # key = char, value = frequency
        countT, window = {}, {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1

        # have is how many reqs our window fulfils, need is how many it needs to
        have, need = 0, len(countT)
        
        res, reslen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update minimum if applicable
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r - l + 1
                
                # pop left
                cl = s[l]
                window[cl] -= 1
                if cl in countT and window[cl] < countT[cl]:
                    have -= 1

                l += 1
            r += 1
        
        l, r = res
        
        return s[l:r+1]
            

