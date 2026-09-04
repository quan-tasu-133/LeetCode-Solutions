class Solution:
    def longestPalindrome(self, s: str) -> str:

        transformed = "^#" + "#".join(s) + "#$"
        n = len(transformed)

        radius = [0] * n
        center = right = 0
        best_center = best_length = 0

        for i in range(1, n - 1):
            mirror = 2 * center - i

            if i < right:
                radius[i] = min(right - i, radius[mirror])

            while (
                transformed[i + radius[i] + 1]
                == transformed[i - radius[i] - 1]
            ):
                radius[i] += 1

            if i + radius[i] > right:
                center = i
                right = i + radius[i]

            if radius[i] > best_length:
                best_center = i
                best_length = radius[i]

        start = (best_center - best_length) // 2
        return s[start:start + best_length]