class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        # using dp to solve this problem
        # sort the jobs by their end time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]

        for s, e, p in jobs:
            # find the first job that ends before the start time of the current job
            i = bisect.bisect(dp, [s + 1]) - 1
            # calculate the profit if we take the current job
            # if we take the current job, the profit will be the current job's profit plus the profit of the job that ends before the start time of the current job
            # if we don't take the current job, the profit will be the same as the profit of the job that ends before the start time of the current job
            # so we compare the two profits and take the maximum one
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]


