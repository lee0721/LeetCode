class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal ans
            if node is None: return 0
            
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            ans = max(ans, node.val + left + right)
            return node.val+ max(left, right)

        dfs(root)
        return ans