# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr != None:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        
        return prev