import heapq
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        num_tasks = Counter(tasks)
        maxheap = [-c for c in num_tasks.values()]
        heapq.heapify(maxheap)
        q = deque()
        time = 0
        while maxheap or q:
            time += 1
            if q and q[0][0] == time:
                _, neg_c = q.popleft()
                heapq.heappush(maxheap, neg_c)

            if maxheap:
                neg_c = heapq.heappop(maxheap)
                neg_c += 1
                if neg_c < 0:
                    q.append((time+n+1, neg_c))
        return time