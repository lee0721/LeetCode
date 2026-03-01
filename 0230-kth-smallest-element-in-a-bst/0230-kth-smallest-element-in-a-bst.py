class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node: Optional[TreeNode]) -> List[int]:
            if node: return inorder(node.left) + [node.val] + inorder(node.right) 
            else: return []
        return inorder(root)[k-1]