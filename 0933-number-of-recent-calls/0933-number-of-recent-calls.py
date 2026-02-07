from collections import deque
class RecentCounter:

    def __init__(self):
        self.windowmilliseconds = 3000
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        cutoff = t - self.windowmilliseconds
        while self.requests and cutoff > self.requests[0]:
            self.requests.popleft()
        return len(self.requests)