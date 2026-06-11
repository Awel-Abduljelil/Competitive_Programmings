class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for string in operations:
            if string == "--X"  or string == "X--":
                X -= 1
            else:
                X += 1
        return X