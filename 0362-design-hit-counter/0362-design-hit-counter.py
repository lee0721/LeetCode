from collections import deque
class HitCounter:

    def __init__(self):
        self.windowseconds = 300
        self.timestamp = deque()

    def hit(self, timestamp: int) -> None:
        self.timestamp.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        cutoff = timestamp - self.windowseconds
        while self.timestamp and cutoff >= self.timestamp[0]:
            self.timestamp.popleft()
        return len(self.timestamp)