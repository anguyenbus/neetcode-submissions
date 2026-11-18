class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF      # 32 bits of 1s
        MAX_INT = 0x7FFFFFFF   # largest positive 32-bit int

        while b != 0:
            carry = (a & b) << 1          # where both bits are 1 -> carry left
            a = (a ^ b) & MASK            # sum without carry, keep 32 bits
            b = carry & MASK              # carry becomes the new thing to add

        # if the top bit is set, a is really a negative number
        return a if a <= MAX_INT else ~(a ^ MASK)
        