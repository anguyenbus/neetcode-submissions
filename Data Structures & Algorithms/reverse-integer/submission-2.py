class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31 - 1               # 2147483647

        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0

        while x != 0:
            x, digit = divmod(x, 10)

            # would res * 10 + digit go over MAX? check BEFORE doing it
            if res > MAX // 10 or (res == MAX // 10 and digit > 7):
                return 0

            res = res * 10 + digit    # push digit onto res

        return sign * res