# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(-1)
        dummy.next = head
        fast, slow = head, head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # save the half and disconnet the list
        second = slow.next
        slow.next = None

        # reverse the second half
        prev = None
        curr = second

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # merge
        first = head
        second = prev 

        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2


        

        

        




        

        

        