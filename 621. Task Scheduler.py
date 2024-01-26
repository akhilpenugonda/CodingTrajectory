class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """        
        # build graph
        graph = collections.defaultdict(set)
        for i in range(len(tasks)):
            graph[tasks[i]].add(i)
        
        # find leaves
        leaves = []
        for i in range(len(tasks)):
            if len(graph[tasks[i]]) == 1:
                leaves.append(i)
        
        # remove leaves level by level
        while len(tasks) > 2:
            lenTasks = len(tasks)
            for leaf in leaves:
                tasks.pop(leaf)
                for key in graph.keys():
                    if leaf in graph[key]:
                        graph[key].remove(leaf)
                if len(graph[tasks[leaf]]) == 1:
                    leaves.append(leaf)
            leaves = leaves[lenTasks:]
        
        return len(tasks)