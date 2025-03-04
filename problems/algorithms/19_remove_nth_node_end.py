# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        leader = head
        follower = head

        for _ in range(n):
            leader = leader.next
        
        if leader == None:
            return head.next

        while leader.next != None:
            follower = follower.next
            leader = leader.next
        follower.next = follower.next.next
        return head