class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.best = 0
    def height(self, node:Optional[TreeNode]) -> int:
        if not node: return -1
        left_h = self.height(node.left)
        right_h = self.height(node.right)

        self.best = max(self.best, left_h + right_h + 2)
        return 1 + max(left_h, right_h)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)
        return self.best