class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            gap = target-num
            if gap in seen: 
                return [seen[gap], i]
            else:
                seen[num] = i
        return []