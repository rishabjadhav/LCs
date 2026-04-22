class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        problem statement: given sorted nums, return nums without duplicates.

        brute force: iterate through nums, remove duplicates when detected

        optimal: removing elements in-place is O(n), because you have to shift remaining elements down.
        instead, use two pointers: a left pointer that sits on a duplicate, and a right pointer on a unique element.
        '''
        # left pointer starts at 1, first element will always stay the same
        l = 1

        for r in range(1, len(nums)):
            # r moves forward unless it is different than it's previous value
            # in that case, we overwrite the left pointer and increment it.
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        
        return l
        

            


