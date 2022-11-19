# https://leetcode.com/problems/find-pivot-index/

class Solution(object):
    def pivotIndex(self, nums):
        sum_total = sum(nums)
        len_arr = len(nums)
        sums_left = {}
        sums_right = {}
        sums_left[0] = 0
        sums_right[0] = sum_total - nums[0]
        sums_right[len_arr-1] = 0
        
        for i in range(len_arr):
            if sums_left[i] == sums_right[i]:
                return i
            
            if i < len_arr-1:
                sums_left[i+1] = sums_left[i]+nums[i]
            if i < len_arr-2:
                sums_right[i+1] = sums_right[i]-nums[i+1]
            
        return -1