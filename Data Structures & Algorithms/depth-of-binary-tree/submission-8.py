# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        problem statement: return the maximum depth of a tree.

        solution: use dfs to store depth reached
        '''
        self.res = 0
        if not root:
            return 0

        def dfs(i, t):
            self.res = max(self.res, t)
            if not i:
                return i
    
            if i.left:
                dfs(i.left, t+1)
            if i.right:
                dfs(i.right, t+1)
        
        dfs(root, 1)
        return self.res
            