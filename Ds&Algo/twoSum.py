#https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):
        diffMap = {target-nums[i]:i for i in range(len(nums))}
        
        for j in range(len(nums)):
            if nums[j] in diffMap.keys() and j != diffMap[nums[j]]:
                return [j, diffMap[nums[j]]]