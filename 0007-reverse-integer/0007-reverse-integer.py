class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        ans = 0

        while x:
            digit = x % 10
            x //= 10

            if ans > (2**31 - 1 - digit) // 10:
                return 0

            ans = ans * 10 + digit

        return sign * ans