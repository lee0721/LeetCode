class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for x, y in points:
            d2 = x * x + y * y
            heapq.heappush(maxheap, (-d2, x, y))
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        return [[x, y] for (_, x, y) in maxheap]