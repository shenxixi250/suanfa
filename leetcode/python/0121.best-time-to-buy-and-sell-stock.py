# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.
# Example 1:
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:
     # Input: [7,6,4,3,1]
     # Output: 0
     # Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 个元素是第i天给定股票的价格。
# 如果只允许您最多完成一笔交易（即买入和卖出一股股票），请设计一种算法以找到最大的利润。
# 请注意，您不能在买股票之前卖出股票。
# 范例1：
# 输入：[7,1,5,3,6,4]
# 输出：5
# 说明：在第2天买入（价格= 1）并在第5天卖出（价格= 6），利润= 6-1 = 5。
              # 不是7-1 = 6，因为销售价格必须大于购买价格。
# 范例2：
# 输入：[7,6,4,3,1]
# 输出：0
# 说明：在这种情况下，不执行任何交易，即最大利润= 0。
# 思路
# 由于我们是想获取到最大的利润，我们的策略应该是低点买入，高点卖出。
# 由于题目对于交易次数有限制，只能交易一次，因此问题的本质其实就是求波峰浪谷的差值的最大值。
# 用图表示的话就是这样：

# 把每个峰值想象成为不一样的一个小山坡 而我们的股票就是由这样一个个小峰值来决定的  我们要做的就测量每一个小山峰的高度来进行 统计    

# 具体步骤是统计每一个 首先要找到我们的山脚  然后找山顶然后去记录这个差值


def stock(L:'List[int]'):
    a=[]
    maxi=0
    mini=L[0]
    for i in L:
        if mini > i:
            mini= i
            a.append(maxi-mini)
            maxi=0
        if i >= maxi :
            maxi = i
            a.append(maxi-mini)
    return max(a)
def maxProfit(prices: 'List[int]'):
    if not prices: return 0
    min_price = float('inf') 
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif max_profit < price - min_price:
            max_profit = price - min_price
    return max_profit
l=[1,2,3,1,5,8]
l=[3,2,1] #如果一直减怎么办没有体现出来
l=[9,8,7,8,7,6]#这种也没有办法解决  看来还是思路不全面的
print(stock(l))
l2=[3,2,1]
print(maxProfit(l2))
l2=[9,8,7,8,7,6]
print(maxProfit(l2))
#我写的太过于纠结 找那个顶点值造成了很多不必要的情况的讨论  南无问题来了我的代码到底问题在哪呢 
