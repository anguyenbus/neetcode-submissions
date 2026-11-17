class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1 # is the lats bit a 1
            n >>= 1 #throw away the last bit
        return count