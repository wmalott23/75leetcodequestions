class Solution(object):
    def maxSubArray(self, nums):
        high = nums[0]
        current = 0
        for x in range(len(nums)):
            if current < 0:
                current = 0
            current += nums[x]
            if current > high:
                high = current
        return high

run = Solution()
print(run.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))