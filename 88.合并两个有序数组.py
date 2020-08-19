#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        leftOffset = len(nums1) - len(nums2) - 1
        rightOffset = len(nums2) - 1

        current = len(nums1) - 1
        while leftOffset >=0  and rightOffset >= 0:
            if nums1[leftOffset] > nums2[rightOffset]:
                nums1[current] = nums1[leftOffset]
                leftOffset -= 1
            else:
                nums1[current] = nums2[rightOffset]
                rightOffset -= 1
            current -= 1

        while rightOffset >= 0:
            nums1[current] = nums2[rightOffset]
            current -= 1
            rightOffset -= 1

# @lc code=end

