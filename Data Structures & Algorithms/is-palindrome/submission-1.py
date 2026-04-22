class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        problem statement: return true if a string is a palindrome, ignoring non-alphanumeric characters and characters
        solution: rewrite string to clean, then use two pointers on either end.
        '''
        ns = ""

        for c in s:
            if c.isalnum():
                ns += c.lower()

        l, r = 0, len(ns) - 1
        while l <= r:
            if ns[l] != ns[r]:
                return False
            l += 1
            r -= 1
        return True