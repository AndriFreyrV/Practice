# https://leetcode.com/problems/number-of-good-pairs/

def sum_n(n):
    return int((n*(n+1))/2)

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numCnt = {}
        for n in nums:
            if n in numCnt.keys():
                numCnt[n] += 1
            else:
                numCnt[n] = 1
        sumOut = 0
        for k in numCnt.keys():
            sumOut+= sum_n(numCnt[k]-1)
        return sumOut
        