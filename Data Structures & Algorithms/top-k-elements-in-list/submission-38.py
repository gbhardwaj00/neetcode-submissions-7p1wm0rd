from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        heap = []
        for num, val in counts.items():
            heapq.heappush(heap, [-val, num])

        res = []
        while len(res) != k:
            res.append((heapq.heappop(heap))[1])

        return res