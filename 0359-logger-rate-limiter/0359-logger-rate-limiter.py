from collections import defaultdict, deque
class Logger:

    def __init__(self):
        self.windowseconds = 10
        self.msgmap = defaultdict(deque)
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        cutoff = timestamp - self.windowseconds
        while self.msgmap[message] and self.msgmap[message][0] <= cutoff:
            self.msgmap[message].popleft()
        if len(self.msgmap[message]) < 1:
            self.msgmap[message].append(timestamp)
            return True
        return False