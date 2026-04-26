class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxW = min(heights[l], heights[r]) * (r - l)

        while l < r:
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            maxW = max(maxW, min(heights[l], heights[r]) * (r - l))

        return maxW
