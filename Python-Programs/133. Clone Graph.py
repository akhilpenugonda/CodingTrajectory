"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution(object):
    def cloneGraph(self, node):
        oldToNew = {}
        def dfs (node):
            if node in oldToNew:
                return oldToNew[node]
            oldToNew[node] = Node(node.val)
            for neighbor in node.neighbors:
                oldToNew[node].neighbors.append(dfs(neighbor))
            return oldToNew[node]
        return dfs(node) if node else None
      