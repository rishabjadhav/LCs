class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        problem statement: return the total number of subarrays in nums that sum to k

        brute force: O(n^2) by computing all subarrays and incrementing counter

        optimal: create frequency table for prefix sums
        * during one pass, compute prefix sum, and check if freq table has prefix that can
        be subtracted from current prefix to equal k. then add this number to result
        '''

        # key = prefix, value = frequency
        freq = {}

        # we do this because a prefix of 0 exists, because not 
        # removing a prefix sum is also an option
        freq[0] = 1

        res = 0
        pref = 0

        for n in nums:
            pref += n

            if pref - k in freq:
                res += freq[pref - k]
            
            freq[pref] = freq.get(pref, 0) + 1
        
        return res