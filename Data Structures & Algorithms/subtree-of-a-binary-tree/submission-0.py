# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        problem: given root and subroot nodes, return true if the subroot's tree
        matches a subroot that's part of root's tree

        first find the subroot in the root's subtrees
        then compare that root's descendents to the subroot's descendents

        call isSameTree on every node in root's subtrees
        '''

        self.res = False

        def isSameTree(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None or p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        def dfs(n):
            if n is None:
                return True
            if isSameTree(subRoot, n):
                self.res = True
            dfs(n.left)
            dfs(n.right)

        dfs(root)
        return self.res