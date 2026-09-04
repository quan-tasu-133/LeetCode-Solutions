from typing import List


class Solution:
    def findMedianSortedArrays(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> float:
        # Binary search trên mảng ngắn hơn
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        a, b = nums1, nums2
        m, n = len(a), len(b)

        total = m + n
        half = (total + 1) // 2

        # Bảo đảm vị trí chia của b luôn hợp lệ
        low = max(0, half - n)
        high = min(m, half)

        while low <= high:
            i = (low + high) // 2
            j = half - i

            # Phần bên trái của a quá lớn
            if i > 0 and j < n and a[i - 1] > b[j]:
                high = i - 1

            # Phần bên trái của b quá lớn
            elif j > 0 and i < m and b[j - 1] > a[i]:
                low = i + 1

            else:
                # Phần tử lớn nhất bên trái
                if i == 0:
                    left_max = b[j - 1]
                elif j == 0:
                    left_max = a[i - 1]
                else:
                    left_max = max(a[i - 1], b[j - 1])

                # Tổng số phần tử lẻ
                if total & 1:
                    return float(left_max)

                # Phần tử nhỏ nhất bên phải
                if i == m:
                    right_min = b[j]
                elif j == n:
                    right_min = a[i]
                else:
                    right_min = min(a[i], b[j])

                return (left_max + right_min) / 2.0