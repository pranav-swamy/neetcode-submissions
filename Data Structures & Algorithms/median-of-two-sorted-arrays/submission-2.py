class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # interchange and make nums1 the smallest array since we will
        # be binary searching that array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        left = 0
        right = len(nums1)

        while left <= right:
            i = left + (right - left) // 2
            # find a j such that it puts 1/2 elts to left and 1/2 elts to right
            # i + j = (m + n) // 2
            # j = (m + n) // 2 - i
            # we are doing (m + n + 1) // 2 - i to have one more left elt when m + n is odd.
            j = (len(nums1) + len(nums2) + 1) // 2 - i

            left1 = nums1[i-1] if i-1 >= 0 else float("-inf")
            left2 = nums2[j-1] if j-1 >=0 else float("-inf")
            right1 = nums1[i] if i < len(nums1) else float("inf")
            right2 = nums2[j] if j < len(nums2) else float("inf")

            if max(left1, left2) <= min(right1, right2):
                # right cut, find median
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
            elif left1 > right2:
                right = i - 1
            else:
                left = i + 1
        

        