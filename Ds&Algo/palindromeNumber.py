# https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        x_str = str(x)
        n = len(x_str)
        if len(x_str) == 1:
            return True
        for i, c in enumerate(x_str):
            if i >= (n/2):
                return True
            if c != x_str[n-i-1]:
                return False