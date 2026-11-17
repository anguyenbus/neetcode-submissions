# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy
        right = head

        # step 1 move right ahead by n
        while n > 0:
            right = right.next
            n -=1
        
        # step 2 move both until right falls off the end
        while right: 
            left = left.next
            right = right.next

        # step 3 skip the target node
        left.next = left.next.next
        return dummy.next