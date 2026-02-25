# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        # create a queue to store nodes whose left and right child have not been swapped yet
        queue = deque([root]) # deque() need iterable obj, TreeNode is not iterable
        # need to put root into list
        while queue:
            current = queue.popleft()
            current.left, current.right = current.right, current.left

            if current.left: queue.append(current.left)
            if current.right: queue.append(current.right)
        return root