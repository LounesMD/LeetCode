from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle0(self, head: Optional[ListNode]) -> bool:
        """
        Complexity: O(n) and O(n)
        """
        if head == None:
            return False
        nodes = dict()

        while head.next != None:
            if head.next in nodes:
                return True
            else:
                nodes[head] = None
                head = head.next

        return False
    
    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        """
        Complexity: O(n) and O(1), but modifies the list
        """
        if head == None:
            return False

        while head.next != None:
            if head.val == None:
                return True
            else:
                head.val = None
                head = head.next

        return False
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Complexity: O(n) and O(1)
        """
        fast = head 
        slow = head 

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
                            
        return False        