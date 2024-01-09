class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
#         # Method 1: Brute Force
#         # Time: O(nlogn)
#         # Space: O(n)
        dist = []
        for point in points:
            dist.append((point[0] ** 2 + point[1] ** 2, point))
        dist.sort()
        res = []
        for i in range(k):
            res.append(dist[i][1])
        return res
#
#         # Method 2: Heap
#         # Time: O(nlogk)
#         # Space: O(k)
#         heap = []
#         for point in points:
#             dist = point[0] ** 2 + point[1] ** 2
#             if len(heap) < k:
#                 heapq.heappush(heap, (-dist, point))
#             else:
#                 heapq.heappushpop(heap, (-dist, point))
#         res = []
#         while heap:
#             res.append(heapq.heappop(heap)[1])
#         return res
#
#         # Method 3: Quick Select
#         # Time: O(n)
#         # Space: O(n)
#         def partition(points, start, end):
        
#             pivot = points[end]
#             i = start - 1
#             for j in range(start, end):
#                 if points[j][0] ** 2 + points[j][1] ** 2 <= pivot[0] ** 2 + pivot[1] ** 2:
#                     i += 1
#                     points[i], points[j] = points[j], points[i]
#             points[i + 1], points[end] = points[end], points[i + 1]
#             return i + 1
#
#         def quickSelect(points, start, end, k):
#             if start <= end:
#                 index = partition(points, start, end)
#                 if index == k:
#                     return
#                 elif index < k:
#                     quickSelect(points, index + 1, end, k)
#                 else:
#                     quickSelect(points, start, index - 1, k)
#
#         quickSelect(points, 0, len(points) - 1, k)
#         return points[:k]

        