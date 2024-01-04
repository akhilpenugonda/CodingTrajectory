class Solution(object):
    def floodFill(self, image, sr, sc, color):
        num_rows = len(image)
        num_columns = len(image[0])
        currentColor = image[sr][sc]
        if(currentColor == color):
            return image
        def dfs(r,c):
            if(image[r][c] == currentColor):
                image[r][c] = color
                if(r >= 1):
                    dfs(r-1, c)
                if(r+1 < num_rows):
                    dfs(r+1, c)
                if(c >= 1):
                    dfs(r, c-1)
                if(c+1 < num_columns):
                    dfs(r, c+1)
        dfs(sr, sc)
        return image