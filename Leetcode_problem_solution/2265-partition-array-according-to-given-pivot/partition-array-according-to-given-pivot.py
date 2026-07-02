class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessThanPivot = []
        equalThanPivot = []
        greaterThanPivot = []

        for i in range(len(nums)):
            if nums[i] < pivot:
                lessThanPivot.append(nums[i])
            elif nums[i] == pivot:
                equalThanPivot.append(nums[i])
            else:
                greaterThanPivot.append(nums[i])
        return lessThanPivot + equalThanPivot + greaterThanPivot