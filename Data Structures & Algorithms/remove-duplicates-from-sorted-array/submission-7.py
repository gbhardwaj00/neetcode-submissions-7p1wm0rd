class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(set(nums))

        j = 0
        for i in range(k):
            while j + 1 < len(nums) - 1 and nums[j] == nums[j + 1]:
                j += 1
            nums[i] = nums[j]
            j += 1

        return k

                
