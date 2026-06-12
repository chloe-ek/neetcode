# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 기존 head 가 변경되니까? dummy 필요한거 아님 ?
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        
        slow, fast = curr, curr 

        # move fast 'n' 만큼
        for _ in range(n):
            fast = fast.next

        # move together 
        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        # slow 에서 fast 이어붙이기 
        slow.next = slow.next.next

        return dummy.next

        
        
        