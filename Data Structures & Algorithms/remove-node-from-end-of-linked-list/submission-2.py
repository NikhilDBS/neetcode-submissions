# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        prev = dummy
        target = count - n
        for _ in range(target):
            prev = prev.next
        prev.next = prev.next.next
        return dummy.next
        