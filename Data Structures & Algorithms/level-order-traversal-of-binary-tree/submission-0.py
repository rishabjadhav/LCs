# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        problem statement: return a list of lists, where each list contains every list at i contains the
        i-th level order traversal.

        solution: use BFS, as we are going level by level, this is the more natural choice. store node val
        and level in queue, and add children to queue as needed. for every enqueued tuple we encounter, add
        to needed list
        '''

        # validation
        if root is None:
            return []

        self.res = [[]]
        
        # use a queue since BFS
        queue = collections.deque()
        queue.append((root, 0))

        while queue:
            # pop the node n and the level it belongs to
            n, lvl = queue.popleft()

            # if a list in self.res doesn't exist for this level, create one
            if len(self.res) - 1 < lvl:
                self.res.append([])

            # append this node's value to it's respective list
            self.res[lvl].append(n.val)


            # enqueue children if applicable
            if n.left:
                queue.append((n.left, lvl + 1))
            if n.right:
                queue.append((n.right, lvl + 1))

        return self.res

