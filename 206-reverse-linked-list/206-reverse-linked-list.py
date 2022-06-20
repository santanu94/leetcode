# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return
        
        result = ListNode(val=head.val)
        head = head.next
        
        while head != None:
            tmp = ListNode(head.val, result)
            head = head.next
            result = tmp
        
        return result