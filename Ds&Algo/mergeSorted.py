# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        outList = ListNode()
        currNode = outList
        while list1 != None or list2 != None:
            if list1 == None:
                currNode.next = list2
                list2 = list2.next
                currNode = currNode.next
            elif list2 == None:
                currNode.next = list1
                list1 = list1.next
                currNode = currNode.next
            else:
                if list2.val < list1.val:
                    currNode.next = list2
                    list2 = list2.next
                    currNode = currNode.next
                else:
                    currNode.next = list1
                    list1 = list1.next
                    currNode = currNode.next
                
        return outList.next