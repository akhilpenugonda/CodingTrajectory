class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
#         # Method 1: BFS
#         # Time: O(mn)
#         # Space: O(mn)
        m = len(mat)
        n = len(mat[0])
        queue = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = -1

        while queue:
            i, j = queue.pop(0)
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and mat[x][y] == -1:
                    mat[x][y] = mat[i][j] + 1
                    queue.append((x, y))

        return mat
        
        