class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxCount = 0
        n = len(nums)
        l, r = 0, 0
        flips = 0

        while r < n:
            if nums[r] == 0:
                flips += 1
            while flips > k:
                if nums[l] == 0:
                    flips -= 1
                l += 1
            maxCount = max(maxCount, r - l + 1) 
            r += 1
            
        return maxCount