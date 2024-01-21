class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral = []
        while matrix:
            spiral += matrix.pop(0)
            matrix = zip(*matrix)[::-1]
        return spiral
    # With out usign zip
    def spiralOrder2(self, matrix):
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        spiral = []
        i, j, di, dj = 0, 0, 0, 1
        for _ in range(m * n):
            spiral.append(matrix[i][j])
            matrix[i][j] = None
            if matrix[(i + di) % m][(j + dj) % n] is None:
                di, dj = dj, -di
            i += di
            j += dj
        return spiral