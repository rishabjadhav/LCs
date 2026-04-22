# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        problem statement: determine the longest path between any two nodes.

        * this is the same as solving max depth in left subtree + max depth in right subtree of a node
            * THIS NODE DOESN'T HAVE TO BE THE root
        
        * on each node, determine max depth on l and r using dfs and store
        * dfs returns the max depth from that node, by recursively calling dfs on left and right nodes
        '''

        # store result of largest diameter
        self.res = 0

        if root is None:
            return 0

        # 
        def dfs(n):
            # base case: return 0 to terminate recursion when n is null
            if n is None:
                return 0
            
            # recurse for left and right depths
            leftdepth = dfs(n.left)
            rightdepth = dfs(n.right)

            # before returning, check diameter at this node, just sum of left and right subtree depths
            self.res = max(self.res, leftdepth + rightdepth)

            # return the max depth of this node, plus 1 for itself
            return max(leftdepth, rightdepth) + 1
        
        dfs(root)
        return self.res
            
            
        
        
        