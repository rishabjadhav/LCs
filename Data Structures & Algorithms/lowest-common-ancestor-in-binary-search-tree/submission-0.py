# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        problem statement: given a BST with unique nodes, and two nodes from the BST,
        return the LOWEST common ancestor of both nodes.
        
        notes
            * the fact that the tree is a BST means that our ancestor must be between p.val and q.val INCLUSIVE
            * start at the root, traverse down BST. we know the root is an ancestor of both nodes.
            * compare root with p or q? probably both.
                * if p and q are less than currNode, recurse to currNode.left
                * if p and q are more than currNode, recurse to currNode.right
                * if we are in-between, we are probably at LCA?
        '''

        def dfs(n):
            if p.val < n.val and q.val < n.val:
                # both p and q are less, recurse down left subtree
                return dfs(n.left)
            elif p.val > n.val and q.val > n.val:
                # both p and q are greater, recurse down right subtree
                return dfs(n.right)
            return n
        
        return dfs(root)