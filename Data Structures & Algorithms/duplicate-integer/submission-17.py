class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # method 1
        # return len(set(nums)) != len(nums)

        # method 2
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
