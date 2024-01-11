class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[y].append(x)  # Fix here: y should be the prerequisite of x
        for i in range(numCourses):
            if(not self.dfs(graph, visited, i)):
                return False
        return True

    def dfs(self, graph, visited, i):
        if(visited[i] == -1):
            return False
        if(visited[i] == 1):
            return True
        visited[i] = -1
        for j in graph[i]:
            #Finding a cycle
            if(not self.dfs(graph, visited, j)):
                return False
        visited[i] = 1
        return True