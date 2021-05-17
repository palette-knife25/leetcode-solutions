#  https://leetcode.com/problems/maximum-subarray/
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        best_sum = -999
        cur_sum = 0
        for x in nums:
            cur_sum = max(x, cur_sum + x)
            best_sum = max(best_sum, cur_sum)
        return best_sum

#####################################################################

soln = Solution()
print(soln.maxSubArray([5,4,-1,7,8]))