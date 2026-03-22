class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        dist = [INF] * n
        dist[src] = 0

        # At most k stops => at most k + 1 flights (edges)
        for _ in range(k + 1):
            temp = dist[:] # just copy dist

            for u, v, price in flights:
                if dist[u] != INF:
                    temp[v] = min(temp[v], dist[u] + price)

            dist = temp

        return -1 if dist[dst] == INF else dist[dst]