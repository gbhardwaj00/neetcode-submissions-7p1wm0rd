class Solution:
    def quickSort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        pivot = nums[len(nums) // 2]
        left = [x for x in nums if x < pivot]
        middle = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]

        return self.quickSort(left) + middle + self.quickSort(right)

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quickSort(nums)

