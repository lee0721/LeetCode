class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, root: TreeNode) -> (bool, int):
        if not root: return True, -1
        leftIsBalanced, leftHeight = self.dfs(root.left)
        if not leftIsBalanced: return False, 0
        rightIsBalanced, rightHeight = self.dfs(root.right)
        if not rightIsBalanced: return False, 0

        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]