class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
    
        left = 0
        max_length = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > 1:
                left += 1
                
            if nums[right] - nums[left] == 1:
                max_length = max(max_length, right - left + 1)
                
        return max_length