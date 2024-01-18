class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timeMap = {}
        
    def binarySearch(self, values, timestamp):
        left = 0
        right = len(values) - 1
        while(left <= right):
            mid = (left + right) // 2
            if(values[mid][1] == timestamp):
                return values[mid][0]
            elif(values[mid][1] > timestamp):
                right = mid - 1
            else:
                left = mid + 1
        return values[right][0]

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
            
        if(key not in self.timeMap):
            self.timeMap[key] = []
        self.timeMap[key].append((value, timestamp))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if(key not in self.timeMap):
            return ""
        else:
            values = self.timeMap[key]
            if(timestamp < values[0][1]):
                return ""
            elif(timestamp >= values[-1][1]):
                return values[-1][0]
            else:
                return self.binarySearch(values, timestamp)
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)