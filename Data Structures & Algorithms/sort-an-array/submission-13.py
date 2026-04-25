import random

class Solution:
    def partition(self, nums, low, high):
        rand_idx = random.randint(low, high)
        nums[rand_idx], nums[high] = nums[high], nums[rand_idx]
        
        pivot = nums[high]  # pick last element as pivot
        i = low - 1         # pointer for smaller elements

        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i+1], nums[high] = nums[high], nums[i+1]  # place pivot
        return i + 1

    def quickSort(self, nums, low, high):
        if low < high:
            pivot_idx = self.partition(nums, low, high)
            self.quickSort(nums, low, pivot_idx - 1)   # sort left
            self.quickSort(nums, pivot_idx + 1, high)  # sort right

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums