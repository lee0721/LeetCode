class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s): return ""

        need = Counter(t)
        win = defaultdict(int)

        needKinds = len(need)
        have = 0

        bestLen = float("inf")
        bestL = 0

        l = 0
        for r, ch in enumerate(s):
            win[ch] += 1
            if ch in need and need[ch] == win[ch]: have += 1

            while have == needKinds:
                curLen = r - l + 1
                if curLen < bestLen:
                    bestLen = curLen
                    bestL = l
                
                left_ch = s[l]
                win[left_ch] -= 1
                if left_ch in need and win[left_ch] < need[left_ch]: have -= 1
                l += 1
        if bestLen == float("inf"): return ""
        return s[bestL: bestL+bestLen]