class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        problem statement: return the length of the longest substring without repeating
        characters of s

        brute force: compute every possible substring, check if it has repeating characters,
        and store max length. this is O(n^2)

        optimal: use sliding window, store frequency of chars in set to check for dupes.

        increment right pointer, once duplicate is found, increment left pointer until no duplicate
        store max length
        '''

        seen = set()
        l, r = 0, 0
        res = 0

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            res = max(res, r - l + 1)
            r += 1

        return res