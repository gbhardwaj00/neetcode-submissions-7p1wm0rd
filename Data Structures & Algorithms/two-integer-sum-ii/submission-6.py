class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # brute force
        # n = len(numbers)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]
        # return []

        # efficient
        # array is sorted, we can use that for two pointers, predciatbale design
        l, r = 0, len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        return []