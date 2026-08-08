class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        n = len(nums)

        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)

        ans = float('inf')

        for left in range(n):
            for length in range(l, r + 1):
                if left + length <= n:
                    total = prefix[left + length] - prefix[left]

                    if total > 0:
                        ans = min(ans, total)

        if ans == float('inf'):
            return -1

        return ans