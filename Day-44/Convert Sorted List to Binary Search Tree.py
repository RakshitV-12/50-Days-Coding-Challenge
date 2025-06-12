# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        mid = self.find_middle(head)
        root = TreeNode(mid.val)
        if head == mid: 
            return root
        root.left = self.sortedListToBST(head) 
        root.right = self.sortedListToBST(mid.next)  

        return root

    def find_middle(self,head):
        """Finds the middle node of the linked list using slow-fast pointers."""
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev: 
            prev.next = None
        return slow
    
