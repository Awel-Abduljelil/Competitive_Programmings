class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        listToString = ""
        for i in nums:
            listToString += str(i)
        return listToString.count(str(digit))
