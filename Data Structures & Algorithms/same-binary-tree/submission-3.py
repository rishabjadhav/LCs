# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        problem statement: return true if p and q are equivalent, and false otherwise

        recurse down tree structure and compare values, while also ensuring non-null

        4 cases:
            p's node is None, q's node is None 
                return True
            p's node is None, q's node is NOT None
                return false
            p's node is NOT None, q's node is None
                return false
            p and q nodes are NOT None
                are p.val == q.val?
                    return True if so, false otherwise
        '''
        self.res = True

        if p is None:
            if q is None:
                # both are none, this is fine
                return True
            else:
                # p is none, q isnt
                return False
        elif q is None:
            # q is none, p isnt
            return False
        
        # neither are null, continue to recurse
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
        