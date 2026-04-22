class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        problem statement: search for target in nums, returning it's index.
        if it doesn't exist in nums, return -1

        solution: use Binary Search!
        '''
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid

        return -1