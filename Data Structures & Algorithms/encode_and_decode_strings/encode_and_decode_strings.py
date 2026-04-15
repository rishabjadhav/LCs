class Solution:
    def encode(self, strs: List[str]) -> str: # encode a list of strings into one string
        res = ""
        
        for s in strs:
            # a string will be encoded with it's length, a # delimiter, and the string itself
            # format: n#string, where n is len(string)
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]: # decode that string back into a list of strings
        strs = []

        # right pointer, between previous string and current string length
        i = 0

        # right pointer should not exceed string length
        while i < len(s):

            # left pointer, between string length and string
            j = i

            # find end of string length
            while s[j] != "#":
                j += 1

            strlen = int(s[i:j])

            strs.append(s[j+1: j+1+strlen])

            i = j + 1 + strlen

        return strs
