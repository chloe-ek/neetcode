# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        tail = dummy

        one = list1
        two = list2

        while one and two:
            if one.val < two.val:
                tail.next = one
                one = one.next
            else:
                tail.next = two
                two = two.next

            tail = tail.next

        if one:
            tail.next = one 
        else:
            tail.next = two

        return dummy.next
            
        