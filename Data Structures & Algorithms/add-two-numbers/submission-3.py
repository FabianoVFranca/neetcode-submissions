# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) 
        current= dummy
        mod = 0
        
        while l1 is not None or l2 is not None:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0 
            soma = l1_val + l2_val + mod
            mod = soma // 10
            soma = soma % 10
            current.next =  ListNode(soma)

            if l1 is not None:
                 l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            current = current.next

        if mod != 0 :
            current.next = ListNode(mod)
        return dummy.next
            

        
            



            


        

        