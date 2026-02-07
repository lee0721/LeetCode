from collections import defaultdict
from typing import DefaultDict, List
from bisect import bisect_right
class TimeMap:

    def __init__(self):
        self.times:DefaultDict[str, List[int]] = defaultdict(list)
        self.values:DefaultDict[str, List[str]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""
        ts = self.times[key]
        idx = bisect_right(ts, timestamp) - 1 
        if idx < 0:
            return ""
        return self.values[key][idx]