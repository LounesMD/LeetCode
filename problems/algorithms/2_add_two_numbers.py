from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Could be refactored to use only one "while l1 or l2 or r" and less variables.
        """
        r = 0
        p = ListNode()
        sol = p

        while l1 != None:
            if(l2 != None):                  
                sum = l1.val + l2.val + r   
                l2 = l2.next
                l1 = l1.next
                r = sum // 10
                sol.next = ListNode(sum % 10)
                sol = sol.next 
                
            else:
                sum = l1.val + r   
                l1 = l1.next
                r = sum // 10
                sol.next = ListNode(sum % 10)
                sol = sol.next 
                
        while l2 != None:
            sum = l2.val + r   
            l2 = l2.next
            r = sum // 10
            sol.next = ListNode(sum % 10)
            sol = sol.next 

        while r > 0:
            sum = r 
            r = sum // 10
            
            sol.next = ListNode(sum % 10)
            sol = sol.next 

        return p.next

l1 = ListNode(2,ListNode(4, ListNode(3)) )
l2 = ListNode(5,ListNode(6, ListNode(4)) )
# l1 = ListNode(0)
# l2 = ListNode(0)
l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

tt = Solution()
res = tt.addTwoNumbers(l1,l2)
while res != None:
    print(res.val)
    res = res.next