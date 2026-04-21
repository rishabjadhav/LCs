class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        problem statement: return the maximum volume of water a container can store,
        where heights[i] represents the height of the i-th bar

        consider: the volume between any two bars i and j is 
        (j - i)(min(height[i], height[j]))

        use two pointers. increment the pointer of shortest height to potentially increase vol.
        '''

        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            vol = (r - l) * min(heights[l], heights[r])
            res = max(res, vol)

            # conditions for moving pointers? we want to maximize volume.

            # we have to make the locally optimal best choice:
                # moving the shorter of the two bars has the best chance of optimizing volume
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return res