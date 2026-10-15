class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # method 1
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen[target - nums[i]], i]
            seen[nums[i]] = i