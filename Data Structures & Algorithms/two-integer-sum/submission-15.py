class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}

        for ind, val in enumerate(nums):
            if target - val in indexMap:
                return [indexMap[target - val], ind]
            indexMap[val] = ind