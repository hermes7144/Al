# 역순 연결리스트
from os import preadv
from typing import List
from typing import Optional
import collections

# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
 

class Solution:
  def reverseList(self, head:ListNode) :
    def reverse(self, node: ListNode, prev: ListNode = None) -> ListNode:
      if not node:
        return prev
      next, node.next = node.next, prev
      return reverse(next, node)
      return

    return reverse(head)
l1 = ListNode(1);
l1.next = ListNode(2);
l1.next.next = ListNode(3);
l1.next.next.next = ListNode(4);
l1.next.next.next.next = ListNode(5);
l1.next.next.next.next.next = ListNode();
