# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()      # fake starting node
        tail = dummy            # last node of the merged list

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1       # attach the list1 node
                list1 = list1.next      # move list1 forward
            else:
                tail.next = list2       # attach the list2 node
                list2 = list2.next      # move list2 forward
            tail = tail.next            # move tail to the new end

        tail.next = list1 if list1 else list2   # attach the leftovers
        return dummy.next