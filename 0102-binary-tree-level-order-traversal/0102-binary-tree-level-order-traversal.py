class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.levels = []
    def helper(self, node: TreeNode, level: int) -> None:
        if len(self.levels) == level:
            self.levels.append([])
        self.levels[level].append(node.val)
        if node.left:
            self.helper(node.left, level+1)
        if node.right:
            self.helper(node.right, level+1)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return self.levels
        self.helper(root, 0)
        return self.levels