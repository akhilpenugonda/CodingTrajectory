class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
            
        if n == 1:
            return [0]

        # build graph
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # find leaves
        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)

        # remove leaves level by level
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    newLeaves.append(neighbor)
            leaves = newLeaves

        return leaves
    
            