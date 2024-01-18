class Solution(object):
    def dfs(self, emailGraph, email, visited, connectedComponent):
            visited.add(email)
            connectedComponent.append(email)
            for neighbor in emailGraph[email]:
                if(neighbor not in visited):
                    self.dfs(emailGraph, neighbor, visited, connectedComponent)
        
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        
        
        # Step 1: Create a dictionary of email to name
        emailToName = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                emailToName[email] = name
        
        # Step 2: Create a graph of email to email
        emailGraph = {}
        for account in accounts:
            firstEmail = account[1]
            for email in account[2:]:
                if(firstEmail not in emailGraph):
                    emailGraph[firstEmail] = set()
                emailGraph[firstEmail].add(email)
                if(email not in emailGraph):
                    emailGraph[email] = set()
                emailGraph[email].add(firstEmail)
        
        # Step 3: DFS on the graph to find the connected components
        visited = set()
        connectedComponents = []
        for email in emailGraph:
            if(email not in visited):
                connectedComponent = []
                self.dfs(emailGraph, email, visited, connectedComponent)
                connectedComponents.append(connectedComponent)
        
        # Step 4: Create the final output
        output = []
        for connectedComponent in connectedComponents:
            name = emailToName[connectedComponent[0]]
            connectedComponent.sort()
            output.append([name] + connectedComponent)
        return output