class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        currsubsets = []
        self.subsetsWithDuphelper(nums, subsets, currsubsets, 0)
        return subsets
    def subsetsWithDuphelper(self, nums, subsets, currsubsets, idx):
        # Add the subset formed so far to the subsets list.
        subsets.append(currsubsets.copy())
        for i in range(idx, len(nums)):
            # If the current element is a duplicate, ignore.
            if i != idx and nums[i] == nums[i-1]:
                continue # same-level duplicate: would start the same subtree again -> duplicate subsets
            currsubsets.append(nums[i])
            self.subsetsWithDuphelper(nums, subsets, currsubsets, i+1)
            currsubsets.pop()