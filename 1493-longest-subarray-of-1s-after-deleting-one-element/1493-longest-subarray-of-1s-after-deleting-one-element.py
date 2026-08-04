class Solution(object):
    def longestSubarray(self, nums):

        l = 0
        zero = 0
        output = 0

        for r in range(len(nums)):

            if nums[r] == 0:
                zero += 1

            while zero > 1:
                if nums[l] == 0:
                    zero -= 1
                l += 1

            output = max(output, r-l)

        return output