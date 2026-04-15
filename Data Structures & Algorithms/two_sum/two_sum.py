class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # returns two indices of nums that sum to target
        # create a dict for nums
        # key: num, val: index
        nms = {}

        # iterate through all nums
        for i in range(len(nums)):
            # check if target - nums[i] is in dict
            if target - nums[i] in nms:
                # this means we've found our complement
                return [i, target - nums[i]]
            
            # if not found, add to dict for later
            nms[nums[i]] = i
