class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = dict()
        largest = 0
        for n in sorted(nums):
            if n - 1 in seq:
                seq[n] = seq[n - 1] + 1
                del seq[n - 1]
            if n not in seq:
                seq[n] = 1
            if seq[n] > largest:
                largest = seq[n]
        return largest