class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseK(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev, cur = None, head
        while k:
            next_temp = cur.next
            cur.next = prev
            prev = cur
            cur = next_temp
            k -= 1
        return prev, head, cur # newHead, newTail, nextStart
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth: return dummy.next

            groupHead = groupPrev.next
            newHead, newTail, nextStart = self.reverseK(groupHead, k)

            groupPrev.next = newHead
            newTail.next = nextStart

            groupPrev = newTail