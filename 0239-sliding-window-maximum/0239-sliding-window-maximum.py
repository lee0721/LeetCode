from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums[:]
        dq = deque()
        out = []

        for i, x in enumerate(nums):
            left_bound = i - k + 1
            while dq and dq[0] < left_bound:
                dq.popleft()
            while dq and nums[dq[-1]] <= x:
                dq.pop()
            dq.append(i)

            if i >= k - 1:
                out.append(nums[dq[0]])
        return out