# https://leetcode.com/problems/linked-list-cycle-ii/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# detect cycle in linked list and return
# cycle start node
class Solution(object):
    def detectCycle(self, head):
        nodeSet = set()
        while head != None:
            nodeSet.add(head)
            
            if head.next in nodeSet:
                return head.next
            
            head = head.next
        
        return None