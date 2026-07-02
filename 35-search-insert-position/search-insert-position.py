class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            middel = (left+right)//2
            if nums[middel] == target:
                return middel
            elif nums[middel] > target :
                right = middel -1 
            else:
                left = middel + 1
        return left
        