class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        min_heap = [(0, k)]
        dist = {}

        while min_heap:
            cur_time, node = heapq.heappop(min_heap)

            if node in dist:
                continue

            dist[node] = cur_time
            for neighbor, weigh in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(min_heap, (cur_time + weigh, neighbor))

        if len(dist) != n:
            return -1

        return max(dist.values())