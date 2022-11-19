# https://leetcode.com/problems/isomorphic-strings/

class Solution(object):
    def isIsomorphic(self, s, t):
        charMap = {}
        mappedChars = set()
        for i, c in enumerate(s):
            if c in charMap.keys() and charMap[c] != t[i]:
                return False
            elif t[i] in mappedChars and c not in charMap.keys():
                return False
        
            else:
                charMap[c] = t[i]
                mappedChars.add(t[i])
        return True