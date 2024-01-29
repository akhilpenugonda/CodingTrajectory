class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """        
        # With formula
        # if not tasks:
        #     return 0
        
        # task_count = collections.Counter(tasks)
        # max_count = max(task_count.values())
        # max_task = len([v for v in task_count.values() if v == max_count])
        # return max(len(tasks), (max_count - 1) * (n + 1) + max_task)

        # Without formula using max heap and queue
        if not tasks:
            return 0
        count = collections.Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()] # in python we have only minheap so we need to negate the values
        # heap will be like [-3, -2, -2]
        heapq.heapify(maxHeap)
        time = 0
        q = collections.deque() # stores [-cnt, idle time]
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) # say we have -3 in top we take it and add 1 to it and push it into queue
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            
        return time