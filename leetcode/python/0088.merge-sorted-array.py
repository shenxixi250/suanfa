# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# Note:
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# Output: [1,2,2,3,5,6]
# 给定两个已排序的整数数组nums1和nums2，合并nums2成nums1为一个排序后的数组。
# 注意：
# 元素的数量在nums1初始化和nums2是m和n分别。
# 你可以假设nums1有足够的空间（尺寸大于或等于m + n）的保存从nums2附加元件。
# 例：
# 输入：
# nums1 = [1,2,3,0,0,0]，M = 3
# nums2 = [2,5,6]，n = 3的
# 输出：[1,2,2,3,5,6]
















#让我联想到之前的两个有序数组的排序问题  和成为一个数组 但是那个题目是可以有额外的空间但是这个题目要求的是原地排序 
def merge(list1,list2)
    list3={}
