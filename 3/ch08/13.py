from typing import List
from typing import Optional
import collections

# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
 

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        current_node = head
        print(head)
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]
    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        # 데크자료형 선언
        q: Deque = collections.deque()
        
        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True
    class Solution:
        def isPalindrome3(self, head: Optional[ListNode]) -> bool:
            rev =None;
            slow = fast = head
            while fast and fast.next:
                fast = fast.next.next;
                rev, rev.next, slow = slow, rev, slow.next
            if fast:
                slow = slow.next
            # 팰린드롬 여부 확인
            while rev and rev.val == slow.val:
                slow, rev = slow.next, rev.next
            return not rev

s1 = Solution()

list1 = ListNode(1);
list1.next = ListNode(2);
list1.next.next = ListNode(2);
list1.next.next.next = ListNode(2);
list1.next.next.next.next = ListNode(1);

print(list1)
print(s1.isPalindrome2(list1));

            


        