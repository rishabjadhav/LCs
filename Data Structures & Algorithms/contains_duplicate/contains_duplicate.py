class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:    # return true if the list contains duplicates
        # define a hash set to hold our unique values
        present = set() 
        
        # iterate through all elements in nums
        for i in nums:
            # if present, duplicate found
            if i in present:
                return True
            else:
                # for all nums, add to set to keep track
                present.add(i)
        return False
