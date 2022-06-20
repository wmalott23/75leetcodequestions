class Solution(object):
    def maxProfit(self, prices):
        min = prices[0]
        profit = 0
        for num in prices:
            if num < min:
                min = num
            if num - min > profit:
                profit = num - min
        print(profit)

run = Solution()
run.maxProfit([7,1,5,3,6,4])