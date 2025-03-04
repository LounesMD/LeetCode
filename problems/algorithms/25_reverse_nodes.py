# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        
        follower, leader = head, head
        cpt = 0
        elt = [0]*k
        while leader != None:
            if cpt < k:
                elt[cpt] = leader.val
                cpt += 1                
                leader = leader.next
            else:
                cpt = 0
                for i in range(1,k+1):
                    follower.val = elt[-i]
                    follower = follower.next
        if k == cpt:
            for i in range(1,k+1):
                follower.val = elt[-i]
                follower = follower.next

        return head
