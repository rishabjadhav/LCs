class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        problem statement: given a string s and integer k, return the longest substring only containing
        one distinct character, once k character replacements are performed

        brute force: compute all possible character replacements on top of all possible substrings, return val

        optimal: use sliding window with character frequency map. if the sum of all non-most-frequent characters
        equals k, this is a valid substring for replacement.

        increment right pointer until valid, then increment left pointer until invalid?
        '''

        l, r = 0, 1
        res = 0

        if s == "":
            return 0

        # key = char, value = frequency of char
        freq = { s[0] : 1 }

        # most frequent char
        mfc = s[0]

        # replacements needed (frequency of non mfc chars in window)
        reps = 0

        while r < len(s):
            print(f"currently on {s[r]}")
            print(f"r = {r}")
            freq[s[r]] = freq.get(s[r], 0) + 1

            print(f"{s[r]} has frequency {freq[s[r]]}")
            
            # update most frequent char if applicable
            if freq[s[r]] > freq[mfc]:
                mfc = s[r]
                print(f"mfc is now {mfc}")
            
            
            reps = (r - l + 1) - freq[mfc]

            if reps > k:
                freq[s[l]] -= 1
                l += 1
            else:
                res = max(res, r - l + 1)
            
            r += 1
        
        return res





