# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def add(self, a, b, _carry):
        carry = 0
        sum = a + b + _carry
        if sum >= 10:
            carry = 1
            sum = sum - 10
            return sum, carry
        return sum, carry
    
    def getMaxLength(self, l1, l2):
        l_l1 = 0
        while l1.next is not None:
            l_l1 += 1
            l1 = l1.next
        
        l_l2 = 0
        while l2.next is not None:
            l_l2 += 1
            l2 = l2.next
        
        return max(l_l1, l_l2)
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # find max length
        max_length = self.getMaxLength(l1, l2)
        answer = None
        head = None
        carry = 0
        # iterate over lists until we get all numbers from list have max length
        for i in range(max_length + 1):
            if l1 is None:
                a = 0
            else:
                a = l1.val
                l1 = l1.next
            if l2 is None:
                b = 0
            else:
                b = l2.val
                l2 = l2.next
        # if shorter one doesn't have any value, it just return zero
            acc, _carry = self.add(a, b, carry)
            carry = 0
        # add two numbers, if there is carry we should pass that through add function
            carry = _carry
            
            if answer is None:
                answer = ListNode(val=acc)
                head = answer
            else:
                answer.next = ListNode(val=acc)
                answer = answer.next
        
        if carry == 1:
            answer.next = ListNode(val=1)
        
        return head
            