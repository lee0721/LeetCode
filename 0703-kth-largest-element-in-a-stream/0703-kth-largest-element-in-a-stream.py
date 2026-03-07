class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = []
        for num in nums:
            self.add(num)
    def add(self, val: int) -> int:
        if len(self.minheap) < self.k or self.minheap[0] < val:
            heapq.heappush(self.minheap, val)
            if len(self.minheap) > self.k:
                heapq.heappop(self.minheap)
        return self.minheap[0]