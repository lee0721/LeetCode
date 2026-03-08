class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxCount = max(freq.values())
        numMax = 0
        for c in freq.values():
            if c == maxCount:
                numMax += 1
        frame = (maxCount - 1) * (n + 1) + numMax
        return max(len(tasks), frame)