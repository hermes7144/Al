from typing import List
from typing import Optional
import collections

# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
 

class Solution:
    def mergeTwoLists(self, l1: ListNode,l2:ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1


l1 = ListNode(1);
l1.next = ListNode(2);
l1.next.next = ListNode(4);

l2 = ListNode(1);
l2.next = ListNode(3);
l2.next.next = ListNode(4);

s1 = Solution()
print(s1.mergeTwoLists(l1, l2));




        