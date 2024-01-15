class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # BFS
        # Time Complexity: O(m*n)
        # Space Complexity: O(m*n)
        
        # Find all rotten oranges
        rotten = []
        fresh = 0
        for i in range(len(grid)):
            # Add code here
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        # BFS
        time = 0
        while rotten:
            new_rotten = []
            for i in range(len(rotten)):
                x, y = rotten[i]
                if x > 0 and grid[x-1][y] == 1:
                    grid[x-1][y] = 2
                    new_rotten.append((x-1,y))
                    fresh -= 1
                if x < len(grid) - 1 and grid[x+1][y] == 1:
                    grid[x+1][y] = 2
                    new_rotten.append((x+1,y))
                    fresh -= 1
                if y > 0 and grid[x][y-1] == 1:
                    grid[x][y-1] = 2
                    new_rotten.append((x,y-1))
                    fresh -= 1
                if y < len(grid[0]) - 1 and grid[x][y+1] == 1:
                    grid[x][y+1] = 2
                    new_rotten.append((x,y+1))
                    fresh -= 1
            rotten = new_rotten
            if rotten:
                time += 1
        
        if fresh == 0:
            return time
        else:
            return -1
        
        