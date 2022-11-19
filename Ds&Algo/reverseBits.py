# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        bit = ''
        rev_value = 0
        val = 0
        i = 32
        while n > 0:
            bit = str(n%2) + bit
            n //= 2
            val += (n%2)*(2**(i))
            i-=1
        print(val)
        leading_zeros = 32-len(bit)
        bit = '0'*leading_zeros + bit # maintain 32 bit format
        
        for i, s in enumerate(bit):
            rev_value += (2**i) * int(s)
        return rev_value