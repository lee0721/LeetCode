class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        currsubsets = []
        self.subsetsWithDuphelper(nums, subsets, currsubsets, 0)
        return subsets
    def subsetsWithDuphelper(self, nums, subsets, currsubsets, idx):
        subsets.append(currsubsets.copy())
        for i in range(idx, len(nums)):
            if i != idx and nums[i] == nums[i-1]:
                continue
            currsubsets.append(nums[i])
            self.subsetsWithDuphelper(nums, subsets, currsubsets, i+1)
            currsubsets.pop()