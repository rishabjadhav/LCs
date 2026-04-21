class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        problem statement: given nums and k, return true if nums contains a "good" subarray
            * a good subarray is one with length at least 2
            * and the sum of its elements is a multiple of k (0, k, 2k, 3k, ...)

        solution: compute prefix sum

        do 2 pointers to determine sum of subarray?
        how do we know whether to increment left or right pointer? what's the signal to do either?
        '''

        # key = prefix sum, value = index

        # prefix sum of 0 means don't remove first element
        pref = { 0 : -1 }

        # running sum for prefix
        rs = 0

        for i in range(len(nums)):
            # update running sum
            rs += nums[i]

            # the following property holds:
                # if two prefix sums share the same result after % k, then their difference's % k == 0
            
            # if another prefix sum with same result after % k is in pref, and their difference in index is sufficient
            if (rs % k) in pref and i - pref[rs % k] > 1:
                return True
            
            # otherwise, store
            if (rs % k) not in pref:
                pref[rs % k] = i
            
            
        return False