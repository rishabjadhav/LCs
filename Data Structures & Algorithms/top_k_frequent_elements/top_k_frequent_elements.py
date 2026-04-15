class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:   # returns k most frequent elements in nums
        # dict, where key = n in nums, value = n count
        count = dict()

        # for each n in nums, get the number of occurences
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # frequency is a list of n lists, where n is the input size of nums
        # each list at freq[i] will hold every element in nums that occurs i times  
        frequency = [[] for i in range(0, len(nums) + 1)]
        
        # populate frequency
        for key, val in count.items():
            frequency[val].append(key)

        result = []

        # iterate through every list in frequency, starting at the top (index n)
        for i in range(len(nums), 0, -1):
            for j in frequency[i]:
                result.append(j)
                if len(result) == k:
                    return result
