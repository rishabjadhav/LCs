class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: # return array output where output[i] is product of all elements in output except nums[i]
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
