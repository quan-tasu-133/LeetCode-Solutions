class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        sign = 1 if x >= 0 else -1
        x *= sign

        while x:
            r = r * 10 + x % 10
            x //= 10

        r *= sign
        return r if -2**31 <= r <= 2**31 - 1 else 0