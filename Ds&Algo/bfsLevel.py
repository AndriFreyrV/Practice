# https://leetcode.com/problems/binary-tree-level-order-traversal/

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object): 
    def bfsLevel(self, root, outLs):
        if root is None:
            return
        
        queue = []
        queue.append((root, 0))
        
        while len(queue) > 0:
            popped = queue.pop(0)
            outLs.append(popped)
            node = popped[0]
            lvl = popped[1]
            
            if node.left != None:
                queue.append((node.left, lvl+1))
 
            if node.right != None:
                queue.append((node.right, lvl+1))
        
        
    def levelOrder(self, root):
        outLs = []
        self.bfsLevel(root, outLs)
        levelList = [(x[0].val, x[1]) for x in outLs]
        
        levelMap = {}
        for x in levelList:
            if x[1] in levelMap.keys():
                levelMap[x[1]].append(x[0])
            else:
                levelMap[x[1]] = [x[0]]
        
        out = []
        for k, v in levelMap.items():
            out.append(v)
        
        return out
            