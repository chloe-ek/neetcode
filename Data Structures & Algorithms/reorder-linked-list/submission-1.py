# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # divide by two 
        slow, fast = head, head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # second list reverse
        second = slow.next 
        slow.next = None # disconnect 

        prev = None 

        while second:
            nxt_node = second.next
            second.next = prev
            prev = second 
            second = nxt_node

        # merge
        first = head 
        second = prev 

        while second:
            tmp1 = first.next # saved next node from first 
            tmp2 = second.next 

            # zigzag connect 
            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2

            




        





        




        

        

        