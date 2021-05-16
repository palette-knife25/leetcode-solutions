#  https://leetcode.com/problems/two-sum/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            comp = target-nums[i]
            if comp in nums:
                ind = nums.index(comp)
                if ind != i:
                    return [i, ind]
                else:
                    continue
            else:
                continue

#####################################################################

sln = Solution()
res = sln.twoSum(nums=[2,7,11,15], target=9)
print(res)