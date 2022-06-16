class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        for num in prices:
            prices2 = prices
            prices2.remove(num)
            for num2 in prices2:
                dif = num2 - num
                if profit < dif:
                    profit = dif
        print(profit)

run = Solution()
run.maxProfit([7,1,5,3,6,4])