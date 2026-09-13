class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            target = -1 * nums[i]
            while j < k:
                if nums[j] + nums[k] == target:
                    triplets.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
        return list(triplets)
