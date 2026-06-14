class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left  = 0
        right =len(nums) - 1
        
        while left <= right:
            middel = (left + right ) // 2
            
            if nums[middel] == target:
                return middel
            if nums[left] <= nums[middel]:
                if nums[left] <= target  < nums[middel]:
                    right = middel- 1
                else:
                    left = middel+ 1
            else:
                if nums[middel] < target <= nums[right]:
                    left = middel + 1
                else:
                    right = middel - 1
                    
        return -1
