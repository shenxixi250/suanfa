# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# Example 1:
# Given nums = [1,1,2],
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the returned length. Example 2:
# Given nums = [0,0,1,1,1,2,2,3,3,4],

# Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
# 给定一个排序后的数组NUMS，除去就地重复的，使得每个元件只出现一次，并返回新长度。
# 不要为另一个数组分配额外的空间，你必须通过修改与O（1）额外的内存就地输入数组做到这一点。
# 实施例1：
# 鉴于NUMS = [1,1,2]，

# 你的函数应该返回长度= 2，用NUMS分别为1和2的前两个元素。
# 思路是使用双指针来解决问题
# 1. 开始时候两个指针指向一个数字
# 2. 如果两个指针指的数值相同,则快指针向前走一步
# 3. 如果不同,两个指针都向前走一步
# 4. 当快指针走完整个数组后,慢指针当前的坐标加一就是数组中不同数字的个数  
def removeDuplicates(num, nums):
    if num:
        slow = 0
        fast= 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast] # 注意这个赋值操作每当快慢不相等的时候就把 慢指针对应的数字给替换了
        return slow + 1
    else:
        return 0
List1=[1,2,3,4,4,4,4,5,5,5,5,6]
print(removeDuplicates(1,List1))
# 大脑模拟一下这个场景  1,2,3,4,4,4,4,5,5,5,6  
# 现在扩展一下 就是当我想把有序的重复元素都删除的时候我要怎么做呢  要求返回一个 重复的list列表   
#和这个题目是一个解   返回list中的前slow+1个数字不就是一个问题了吗
