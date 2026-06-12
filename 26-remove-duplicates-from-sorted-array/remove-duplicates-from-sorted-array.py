class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ordered = sorted(list(set(nums)))
        for i in range(len(ordered)):
            nums[i] = ordered[i]
        return len(ordered)