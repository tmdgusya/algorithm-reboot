from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # easy way to solve
        # just save elements into deque, and pop it from end of the queue
        if head is None:
            return None

        queue = deque()
        pointer = head
        # O(N)
        while pointer is not None:
            queue.appendleft(pointer.val)
            pointer = pointer.next

        head = None
        curr = head
        # O(N)
        while len(queue) != 0:
            popped = queue.popleft()
            if curr is None:
                head = ListNode(popped)
                curr = head
            else:
                new = ListNode(popped)
                curr.next = new
                curr = new

        return head