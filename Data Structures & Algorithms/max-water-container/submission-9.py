class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxW = 0
        
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            maxW = max(maxW, area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                r -= 1 
                l += 1
        
        return maxW
            