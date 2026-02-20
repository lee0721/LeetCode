class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums2, nums1 = nums1, nums2
        m, n = len(nums1), len(nums2)
        total = m+n
        half = (total+1)//2

        l, r = 0, m
        NEG_INF = float("-inf")
        POS_INF = float("inf")
        while l <= r:
            i = (l+r)//2
            j = half - i

            left1 = nums1[i - 1] if i > 0 else NEG_INF
            right1 = nums1[i] if i < m else POS_INF
            left2 = nums2[j - 1] if j > 0 else NEG_INF
            right2 = nums2[j] if j < n else POS_INF

            if left1 <= right2 and left2 <= right1:
                if total % 2 == 1:
                    return float(max(left1, left2))
                return (max(left1, left2) + min(right1, right2)) / 2.0

            if left1 > right2:
                r = i - 1
            else:
                l = i + 1