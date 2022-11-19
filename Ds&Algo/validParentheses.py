# https://leetcode.com/problems/valid-parentheses/submissions/

class Solution(object):
    def isValid(self, s):
        match_dict = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stack = []
        for c in s:
            if c in match_dict.keys():
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                p = stack.pop()
                if match_dict[p] != c:
                    return False
        if len(stack) != 0:
            return False
        return True