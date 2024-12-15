# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        slow = fast = head 
        prev = None
        while slow:
            nextnode = slow.next 
            slow.next = prev 
            prev = slow
            slow = nextnode
        return prev
        