class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # all triplets where a + b + c = 0
        # idx i, j, k distinct
        # no duplicate triplets
        # ourput in any order

        # brute force, O(n^3)
        # triplets = set() 
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         for k in range(j + 1, n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 triplets.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        # return [list(triplet) for triplet in triplets]

        # O(n^2) by using pair sum, with the property that if a + b + c = 0 => b + c = -a
        # we will use two pointers pair sum 
        # need a sorted array
        nums.sort()
        triplets = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            pairs = self.pairSum(i + 1, nums, -nums[i])

            for p in pairs:
                triplets.append([nums[i]] + p)

        return triplets

    def pairSum(self, startIdx, nums, target):
        pairs = []

        l, r = startIdx, len(nums) - 1
        while l < r:
            sum = nums[l] + nums[r]
            if sum == target:
                pairs.append([nums[l], nums[r]])
                l += 1

                while l < r and nums[l] == nums[l - 1]:
                    l += 1
            elif sum < target:
                l += 1
            else:
                r -= 1
        return pairs
                
        



