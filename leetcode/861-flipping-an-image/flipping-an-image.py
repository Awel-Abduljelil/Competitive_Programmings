class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        temp = []
        for i in range(n):
            temp.append(list(image[i]))
            for j in range(n):
                image[i][j] = abs(temp[i][n-1-j]-1)
        return image