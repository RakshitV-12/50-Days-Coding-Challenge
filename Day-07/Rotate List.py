# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        k = k % length
        if k == 0:
            return head
        current = head
        for _ in range(length - k - 1):
            current = current.next
        new_head = current.next
        current.next = None
        tail = new_head
        while tail.next:
            tail = tail.next
        tail.next = head
        return new_head

