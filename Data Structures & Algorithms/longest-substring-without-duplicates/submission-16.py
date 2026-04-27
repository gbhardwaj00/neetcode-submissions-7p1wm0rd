class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, n = 0, 0, len(s)
        res = 0
        seen = set()
        
        while r < n:
            if s[r] not in seen:
                seen.add(s[r])
                res = max(res, r - l + 1)
                r += 1
            else:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                seen.remove(s[l])
                l += 1
        
        return res

            