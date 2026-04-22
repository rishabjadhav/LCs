# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        problem statement: return true if the binary tree is height isBalanced
            * a height-balanced tree is one where the left and right subtrees of every node differ
            by no more than one

        solution: use dfs to recursively compute left and right subtree depths, while checking differences in between
        '''

        self.res = True

        if root is None:
            return True

        def dfs(n):
            if n is None:
                return 0
            
            # compute left and right depths recursively
            leftdepth = dfs(n.left)
            rightdepth = dfs(n.right)

            # if the difference in this node's left and right subtree depth is more than 1, tree isn't balanced
            if abs(leftdepth - rightdepth) > 1:
                self.res = False
            
            # return depth of this node
            return max(leftdepth, rightdepth) + 1

        dfs(root)
        return self.res