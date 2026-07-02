class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        given_num = "".join([str(x) for x in digits])
        output = list(map(int,str(int(given_num)+1)))
        return output
        
