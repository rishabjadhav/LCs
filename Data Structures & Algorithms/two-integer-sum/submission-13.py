class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key, num, value, index
        dc = {}

        for i in range(len(nums)):
            # check if the counterpart in dc
            if target - nums[i] in dc:
                return [dc[target - nums[i]], i]
            
            dc[nums[i]] = i
