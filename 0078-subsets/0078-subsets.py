class Solution:
    def subsets(self, nums):
        self.output = []
        self.n = len(nums)
        self.backtrack(0, [], nums)
        return self.output

    def backtrack(self, first, curr, nums):
        self.output.append(curr.copy()) # Add the current subset to the output
        # Generate subsets starting from the current index
        for i in range(first, self.n):
            curr.append(nums[i])
            self.backtrack(i + 1, curr, nums)
            curr.pop()