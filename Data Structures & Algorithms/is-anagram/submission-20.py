class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # method 1
        # s_set = {}
        # t_set = {}

        # for i in range(len(s)):
        #     s_set[s[i]] = s_set.get(s[i], 0) + 1
        #     t_set[t[i]] = t_set.get(t[i], 0) + 1
        
        # return s_set == t_set

        # method 2
        return Counter(s) == Counter(t)