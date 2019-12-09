# 英语原题
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
# 给定一个整数数组NUMS，发现其具有最大和的连续子阵列（含有至少一个数字），并返回它的总和。
# 例：
# 输入：[-2,1，-3,4，-1,2,1，-5,4]，
# 输出：6
# 说明：[4，-1,2,1]具有最大总和= 6。
# 跟进：
# 如果你已经知道了O（n）的解决方案，尝试编码使用分而治之的方法，这是比较微妙的另一种解决方案。
def baoli(list1):
    for i in range(1,len(list1)):
        j=i
        for j in range(i,len(list1)):
            add=sum(list1[i-1:j])
            if j==1:
                 max1=add
            if add>max1:
                 max1=add
    print(max1)
#暴力法的基础上我们可以使用 前缀来解也就是 数组中前n个数值的和我们先算出来然后放到一个数组上去  
# 数组的第n个元素 到第m个元素的值我们就可以使用简单  b[m]-b[n-1]来进行表示了  这样节省下来了n的实践度  
def xiuhu(list1):
    b={}
    for k in range(1,len(list1)):
        b[k]=sum(list1[0:k])
    for i in range(1,len(list1)):
        j=i
        for j in range(i,len(list1)):
            add=b[j]-b[i]
            if j==1:
                 max1=add
            if add>max1:
                 max1=add
    print(max1)
# 解法三 - 优化前缀和 - from @lucifer
# 我们定义函数 S(i) ，它的功能是计算以 0（包括 0）开始加到 i（包括 i）的值。
# 那么 S(j) - S(i - 1) 就等于 从 i 开始（包括 i）加到 j（包括 j）的值。
# 我们进一步分析，实际上我们只需要遍历一次计算出所有的 S(i), 其中 i = 0,1,2....,n-1。 然后我们再减去之前的 S(k),其中 k = 0，1，i - 1，中的最小值即可。 因此我们需要 用一个变量来维护这个最小值，还需要一个变量维护最大值。
def xiuhu2(list1):
    b={}
    for k in range(1,len(list1)):
        b[k]=sum(list1[0:k])
    for i in range(1,len(k)):
        min=max=b[0]
        if min>b[i]:
            min=b[i]
        if max<b[i]:
            max=b[i]
    print(max-min)
# 我们把数组nums以中间位置（m)分为左（left)右(right)两部分. 那么有， left = nums[0]...nums[m - 1] 和 right = nums[m + 1]...nums[n-1]
# 最大子序列和的位置有以下三种情况：
    # 考虑中间元素nums[m], 跨越左右两部分，这里从中间元素开始，往左求出后缀最大，往右求出前缀最大, 保持连续性。
    # 不考虑中间元素，最大子序列和出现在左半部分，递归求解左边部分最大子序列和
    # 不考虑中间元素，最大子序列和出现在右半部分，递归求解右边部分最大子序列和
# 分别求出三种情况下最大子序列和，三者中最大值即为最大子序列和。
# 举例说明，如下图： 
# import sys
# class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
        # return self.helper(nums, 0, len(nums) - 1)
    # def helper(self, nums, l, r):
        # if l > r:
            # return -sys.maxsize
        # mid = (l + r) // 2
        # left = self.helper(nums, l, mid - 1)
        # right = self.helper(nums, mid + 1, r)
        # left_suffix_max_sum = right_prefix_max_sum = 0
        # sum = 0
        # for i in reversed(range(l, mid)):
            # sum += nums[i]
            # left_suffix_max_sum = max(left_suffix_max_sum, sum)
        # sum = 0
        # for i in range(mid + 1, r + 1):
            # sum += nums[i]
            # right_prefix_max_sum = max(right_prefix_max_sum, sum)
        # cross_max_sum = left_suffix_max_sum + right_prefix_max_sum + nums[mid]
        # return max(cross_max_sum, left, right)
        # 分治法看不懂啊
# 动态规划的难点就是找到递推公式
# 动态规划法
# 1. 若记b[j]=max(a[i]+a[i+1]+..+a[j]),其中1<=i<=j,并且1<=j<=n。则所求的最大子段和为max b[j]，1<=j<=n。
# 2. 由b[j]的定义可易知，当b[j-1]>0时b[j]=b[j-1]+a[j]，否则b[j]=a[j]。故b[j]的动态规划递归式为:
# b[j]=max(b[j-1]+a[j],a[j])，1<=j<=n
# 而b[j]的其实值就是a[0] 所以我们可以通过这个公式来继续下去我们的递推公式
# 状态转移方程为： dp[i] = max(dp[i - 1] + nums[i], nums[i])
# 初始化：dp[0] = nums[0]
# 从状态转移方程中，我们只关注前一个状态的值，所以不需要开一个数组记录位置所有子序列和，只需要两个变量，
# currMaxSum - 累计最大和到当前位置i
# maxSum - 全局最大子序列和:
    # currMaxSum = max(currMaxSum + nums[i], nums[i])
    # maxSum = max(currMaxSum, maxSum)
def dongtaiguihua(list1):
    b={}
    b[0]=list1[0]
    maxSum=b[0]
    for i in range(1,len(list1)):
        b[i]=max(b[i-1]+list1[i],list1[i])#b[i] 这个数组表示的是当前的我们的数组总第一个到最后到第n个到最后的当前子序列的最大值
        maxSum=max(b[i],maxSum)
    print(maxSum)
l=[-2,1,-3,4,-1,2,1,-5,4]
baoli(l)
xiuhu(l)
xiuhu(l)
dongtaiguihua(l)
