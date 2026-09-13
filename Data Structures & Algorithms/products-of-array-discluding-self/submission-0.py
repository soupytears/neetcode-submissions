from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totals = list()
        for i in range(len(nums)):
            totals.append(prod(nums[:i])) 
            if i < len(nums) + 1:
                totals[i] *= prod(nums[i+1:])
        return totals