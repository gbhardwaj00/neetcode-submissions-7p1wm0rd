class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l1 = len(s)
        l2 = len(t)
        
        if l2 > l1:
            return ""

        countT = Counter(t)
        window = defaultdict(int)
        have = 0
        need = len(countT)
        res = ""

        l = 0
        r = 0
        while r < len(s):
            window[s[r]] += 1
            if window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                if res == "" or (r - l + 1) < len(res):
                    res = s[l:r+1]
                window[s[l]] -= 1
                if window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

            r += 1

        return res   


                



