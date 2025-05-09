# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = slow = head
        for _ in range(k - 1):
            fast = fast.next

        first_k_node = fast
        temp = fast

        while temp.next:
            temp = temp.next
            slow = slow.next

        first_k_node.val, slow.val = slow.val, first_k_node.val

        return head
