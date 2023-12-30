class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            for i in s:
                if i in t:
                    t = t.replace(i, '', 1)
                else:
                    return False

            return True
            
    # optimized solution
    def isAnagram2(self, s, t):
        return sorted(s) == sorted(t)
    
    # optimized solution
    def isAnagram3(self, s, t):
        if len(s) != len(t):
            return False
        else:
            return sorted(s) == sorted(t)
    
    # optimized solution characterwise using dictionary
    def isAnagram4(self, s, t):
        if len(s) != len(t):
            return False
        else:
            dict1 = {}
            dict2 = {}
            for i in s:
                dict1[i] = dict1.get(i, 0) + 1
            for i in t:
                dict2[i] = dict2.get(i, 0) + 1
            return dict1 == dict2
    