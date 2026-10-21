class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = [0] * len(nums)
        i = 0

        for num in nums:
            if num != 0:
                temp[i] = num
                i += 1
        
        for j in range(len(nums)):
            nums[j] = temp[j]
        