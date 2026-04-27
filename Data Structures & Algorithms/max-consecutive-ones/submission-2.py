class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r, res = 0, 0, 0
        n = len(nums)

        while r < n:
            while r < n and nums[r] != 0:
                r += 1
            res = max(res, r - l)
            while r < n and nums[r] != 1:
                r += 1
                l = r

        return res


