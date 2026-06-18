class Solution:
    def reverseWords(self, s: str) -> str:
        stringToList = s.split(" ")
        for i in range(len(stringToList)):
            stringToList[i] = stringToList[i][::-1]
        return " ".join(stringToList)