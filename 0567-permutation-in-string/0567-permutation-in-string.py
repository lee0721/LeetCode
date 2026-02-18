class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        def idx(ch: str) -> int:
            return ord(ch) - ord('a')
        need = [0]*26
        win = [0]*26

        for ch in s1:
            need[idx(ch)] += 1
        
        for i in range(len(s1)):
            win[idx(s2[i])] += 1

        if win == need: return True

        l = 0
        for r in range(len(s1), len(s2)):
            win[idx(s2[r])] += 1
            win[idx(s2[l])] -= 1
            l += 1

            if win == need: return True
        return False