class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if(len(s) < len(p)):
            return []
        #sliding window method
        #create a dictionary for p
        p_dict = {}
        for i in p:
            if i in p_dict:
                p_dict[i] += 1
            else:
                p_dict[i] = 1
        #create a dictionary for s
        s_dict = {}
        for i in range(len(p)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1
        #compare the two dictionaries
        result = []
        if s_dict == p_dict:
            result.append(0)
        #sliding window
        for i in range(len(p), len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1
            #remove the first element in the window
            s_dict[s[i-len(p)]] -= 1
            if s_dict[s[i-len(p)]] == 0:
                del s_dict[s[i-len(p)]]
            if s_dict == p_dict:
                result.append(i-len(p)+1)
        return result
    
    # def findAnagrams(self, s: str, p: str) -> List[int]:
        hm, res, pL, sL = defaultdict(int), [], len(p), len(s)
        if pL > sL: return []

        # build hashmap
        for ch in p: hm[ch] += 1

        # initial full pass over the window
        for i in range(pL-1):
            if s[i] in hm: hm[s[i]] -= 1
            
        # slide the window with stride 1
        for i in range(-1, sL-pL+1):
            if i > -1 and s[i] in hm:
                hm[s[i]] += 1
            if i+pL < sL and s[i+pL] in hm: 
                hm[s[i+pL]] -= 1
                
            # check whether we encountered an anagram
            if all(v == 0 for v in hm.values()): 
                res.append(i+1)
                
        return res