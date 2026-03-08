class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxheap = [(-c, task) for task, c in freq.items()]
        heapq.heapify(maxheap)

        time = 0
        cooldown = deque()
        while maxheap or cooldown:
            time += 1
            while cooldown and cooldown[0][0] == time:
                _, neg_cnt, task = cooldown.popleft()
                heapq.heappush(maxheap, (neg_cnt, task))
            if maxheap:
                neg_cnt, task = heapq.heappop(maxheap)
                neg_cnt += 1
                if neg_cnt != 0: 
                    cooldown.append((time + n + 1, neg_cnt, task))
        return time