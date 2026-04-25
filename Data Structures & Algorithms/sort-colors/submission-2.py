class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0]*3
        for n in nums:
            counts[n] += 1

        curIdx = 0
        for i, v in enumerate(counts):
            j = v
            while j > 0:
                nums[curIdx] = i
                curIdx += 1
                j -= 1
        

        