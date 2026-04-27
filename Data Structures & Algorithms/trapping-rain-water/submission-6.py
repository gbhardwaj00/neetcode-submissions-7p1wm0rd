class Solution:
    def trap(self, height: List[int]) -> int:
        # left max and right max
        n = len(height)
        leftMax = [0]*n
        rightMax = [0]*n

        i = 1
        r = n - 2

        while i < n:
            leftMax[i] = max(height[i - 1], leftMax[i - 1])
            i += 1

        while r >= 0:
            rightMax[r] = max(rightMax[r + 1], height[r + 1])
            r -= 1

        res = 0
        for i in range(n):
            res += max(0, min(leftMax[i], rightMax[i]) - height[i])

        return res
        