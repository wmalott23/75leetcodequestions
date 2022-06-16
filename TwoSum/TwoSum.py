class Solution(object):
    def twoSum(self, nums, target):
        answer = []
        for idx, num in enumerate(nums):
            nums2 = nums[:]
            del nums2[idx]
            for idy, num2 in enumerate(nums2):
                if num == target - num2:
                    answer.append(idx)
                    v = idy + 1
                    answer.append(v)
                    return(answer)

run = Solution()
print(run.twoSum([-1, -2, -3, -4, -5], -8))