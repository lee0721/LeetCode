from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            cnt = [0]*26
            for c in s:
                cnt[ord(c)-ord("a")] += 1
            groups[tuple(cnt)].append(s)
        return list(groups.values())