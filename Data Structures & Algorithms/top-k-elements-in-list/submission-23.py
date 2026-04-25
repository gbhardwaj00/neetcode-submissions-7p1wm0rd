from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        max_heap = [[-freq, num] for num, freq in counts.items()]

        heapq.heapify(max_heap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(max_heap)[1])

        return res