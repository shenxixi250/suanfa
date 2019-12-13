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

# 看了下面的那个解题过程我们大致也有了类似的思路  就是但是问题就是现在我们不能够新创建
# 数组list3 这个问题  但是我们现在有一个list1 这个数组比较长[1,2,3,0,0,0]
# 后面的那三个0的位置就可一为保存一个新的元素放进去  所以这个题目转化就是 list1 我们看成123 list2是256  list3 实际上是list1倒过来我们在一一填充的 
# 从后面比较从后面往前来进行填充的
# 具体操作看图  https://github.com/azl397985856/leetcode/blob/master/problems/88.merge-sorted-array.md 














#让我联想到之前的两个有序数组的排序问题  和成为一个数组 但是那个题目是可以有额外的空间但是这个题目要求的是原地排序 
def merge(list1,list2):
    list3={}
    i=j=t=0
    while True:
        if i>=len(list1):
            for j in range(j,len(list2)):
                list3[t]=list2[j]
                t+=1
            break
        if j>=len(list2):
            for i in range(i,len(list1)):
                list3[t]=list1[i]
                t+=1
            break
        if(list1[i]<list2[j]):
            list3[t]=list1[i]
            i+=1
        else:
            list3[t]=list2[j]
            j+=1
        t+=1
    print(list3)

l1=[1,2,4,6,8]
l2=[2,4,5,6,8,45,67,78]
merge(l1,l2)
