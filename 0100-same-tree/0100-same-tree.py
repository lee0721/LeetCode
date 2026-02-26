class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def check(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
        return True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        deq = deque([(p, q)]) 
        #use tuple to store p and q and use list to pack them bc deque() need the iterable obj
        while deq:
            p, q = deq.popleft()
            if not self.check(p, q): return False
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        return True