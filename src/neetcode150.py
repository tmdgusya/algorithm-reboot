from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Both are already sorted in order.
        # So, what i need to do is just check
        need_to_loop = True
        merged_list = ListNode(-1)
        left = list1
        right = list2
        _merged_list = merged_list
        while need_to_loop:
            if left is None:
                need_to_loop = False
                while right is not None:
                    _merged_list.next = ListNode(right.val)
                    right = right.next
                    _merged_list = _merged_list.next
                break
            if right is None:
                need_to_loop = False
                while left is not None:
                    _merged_list.next = ListNode(left.val)
                    left = left.next
                    _merged_list = _merged_list.next
                break

            if left.val > right.val:
                _merged_list.next = ListNode(right.val)
                _merged_list = _merged_list.next
                right = right.next
                continue
            if right.val > left.val:
                _merged_list.next = ListNode(left.val)
                _merged_list = _merged_list.next
                left = left.next
                continue
            if right.val == left.val:
                _merged_list.next = ListNode(left.val)
                _merged_list = _merged_list.next
                left = left.next
                _merged_list.next = ListNode(right.val)
                _merged_list = _merged_list.next
                right = right.next
                continue


        return merged_list.next