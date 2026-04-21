class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        problem statement: return all triplets (3 element lists) where all elements sum to 0, 
        and all elements' indices are unique. no duplicates.

        brute force: triple nested for loop, put triplets in a set to nuke duplicates, check that i, j, k are unique

        optimal: sort to avoid duplicates and use two pointers adjust 3Sum
            * use unique starting number every go-around
            * use 2 pointers from i+1 (left) and end of list (r)
            * return all unique triplets
        '''

        res = []
        nums.sort()
        
        for i in range(len(nums)):
            # don't reuse starting element if we aren't on first element
            # if we aren't and this element is the same as the previous one, skip to avoid pushing duplicate triplets to res
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # left + right pointers on opposite sides of remaining elements
            l, r = i + 1, len(nums) - 1

            while l < r:
                currsum = nums[i] + nums[l] + nums[r]
                if currsum > 0:
                    r -= 1
                elif currsum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    # push left pointer up, don't worry about right pointer it will decrement if needed
                    l += 1

                    # new left pointer shouldn't be at same element again
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
            
        return res