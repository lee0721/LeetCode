# 981 Time Based Key-Value Store
from bisect import bisect_right
from collections import defaultdict
from typing import DefaultDict, List

class TimeMap:
    def __init__(self):
        # key -> sorted timestamps / values (timestamps are appended in increasing order)
        self.times: DefaultDict[str, List[int]] = defaultdict(list)
        self.values: DefaultDict[str, List[str]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Assumption (LeetCode): timestamps for the same key are non-decreasing
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""
        ts_list = self.times[key]
        idx = bisect_right(ts_list, timestamp) - 1  # last ts <= timestamp
        if idx < 0:
            return ""
        return self.values[key][idx]

"""Evaluate:
TC:
- set: O(1) amortized (append)
- get: O(log n) per query, where n = number of versions for that key (binary search)

SC:
- O(total_set_calls) to store all (timestamp, value) versions
"""
