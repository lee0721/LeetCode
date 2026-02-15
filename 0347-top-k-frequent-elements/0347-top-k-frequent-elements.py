from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        for num, freq in cnt.items():
            buckets[freq].append(num)
        res = []
        for freq in range(len(buckets)-1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k: return res
        return res