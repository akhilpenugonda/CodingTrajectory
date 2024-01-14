class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid, r, c):
            if(grid[r][c] == '0'):
                return
            grid[r][c] = '0'
            if(r-1 >= 0):
                dfs(grid, r-1, c)
            if(r+1 < len(grid)):
                dfs(grid, r+1, c)
            if(c-1 >= 0):
                dfs(grid, r, c-1)
            if(c+1 < len(grid[0])):
                dfs(grid, r, c+1)
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if(grid[r][c] == '1'):
                    dfs(grid, r, c)
                    count += 1
        return count
    
