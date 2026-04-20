class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        problem statement: return t/f if by prerequisites, all courses can be finished

        prerequisites[i] = [a, b] indicates that b is a prereq to a, or that you must take b before a

        THIS IS JUST TOPOLOGICAL SORT! We want to determine if an ordering exists such that A DOES NOT appear
        before B in the sort if B -> A is an edge in the graph.

        Therefore, we have to determine that no cycles take place in our graph, as cycles make topo sort impossible.
        We use DFS here to detect cycles.
        '''

        # numCourses empty lists in a list makes our adjacency list
        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            # b -> a is an edge in our graph
            adj[b].append(a)
        
        # now we have to detect cycles, we can use DFS for this
        # if we end up revisiting a visited node, it's false

        # 0 is unvisited (default), 1 is visiting in current path, 2 is processed
        # all nodes start unvisited
        state = [0] * numCourses

        def dfs(n):
            # if node in current path has already been visited, cycle detected, return False
            if state[n] == 1:
                return False

            # if we've already called DFS on this node, no need to run it again
            if state[n] == 2:
                return True
            
            # by this point, we know this node was unvisited, now we declare it as processed
            state[n] = 1
            
            # call DFS on all nodes in this node's adj list, if any of those calls return false, return as false
            for x in adj[n]:
                if dfs(x) == False:
                    return False
            
            # if the entire adjacency list is good, we return True
            state[n] = 2
            return True
        
        # call DFS on every node in case graph is not connected
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        
        return True
