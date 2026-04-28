class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countA = Counter(s1)
        countB = Counter(s2[:len(s1)])
        
        l = 0
        r = len(s1)
        n = len(s2)

        while r < n:
            if countA == countB:
                return True
            countB[s2[l]] -= 1
            if countB[s2[l]] == 0:
                del countB[s2[l]]
            l += 1
            countB[s2[r]] += 1
            r += 1

        return countA == countB
            
        



