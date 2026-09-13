class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num2 = dict()
        for i, num in enumerate(nums):
            if (target - num) in num2:
                return [num2[target - num], i]
            num2[num] = i
        return [0, 0] 