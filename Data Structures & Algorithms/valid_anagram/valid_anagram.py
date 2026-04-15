class Solution:
    def isAnagram(self, s: str, t: str) -> bool:    # returns true if strings s and t are anagrams of eachother
        # anagrams must be same length
        if len(s) != len(t):
            return False

        # key: char, val: number of occurences
        ds = {}
        dt = {}

        # wcount
        wcounts = [0] * 26
        wcountt = [0] * 26

        for i in range(0, len(s)):
            # for each char in s and t, increment 1 to occurences 
            ds[s[i]] = ds.get(s[i], 0) + 1
            dt[t[i]] = dt.get(t[i], 0) + 1

            wcounts[ord(s[i]) - ord('a')] += 1
            wcountt[ord(t[i]) - ord('a')] += 1

        # by here we've counted occurences, now we compare

        return wcounts == wcountt
        
        # or alternatively
        # return ds == dt

