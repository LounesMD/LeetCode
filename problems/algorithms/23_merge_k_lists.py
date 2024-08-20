from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Complexity: O(n * k * log(k))
        """
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            if lists[0] == None:
                return lists[1]
            elif lists[1] == None:
                return lists[0]
            
            elif lists[0].val < lists[1].val:
                return ListNode(lists[0].val, self.mergeKLists([lists[0].next, lists[1]]))
            else:
                return ListNode(lists[1].val, self.mergeKLists([lists[0], lists[1].next]))
        else:
            return self.mergeKLists(
                [
                    self.mergeKLists(lists[:len(lists)//2]),
                    self.mergeKLists(lists[len(lists)//2:])
                ]
            )

sol = Solution()
l = [[1,4,5],[1,3,4]]
l = [ListNode(1,ListNode(4, ListNode(5))),
     ListNode(1,ListNode(3, ListNode(4))),
     ListNode(1,ListNode(2)),
     ]
res = sol.mergeKLists(l)
while res != None:    
    print(res.val)
    res = res.next
