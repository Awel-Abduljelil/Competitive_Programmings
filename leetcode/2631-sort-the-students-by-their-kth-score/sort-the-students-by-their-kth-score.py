class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        k_th_score = {}
        for i in range(len(score)):
            value = score[i][k]
            k_th_score[value] = i
        sorted_score = sorted(k_th_score.keys(),reverse=True)
        final_matrix = []
        for j in range(len(score)):
            key = sorted_score[j]
            indexOfScore = k_th_score[key]
            final_matrix.append(score[indexOfScore]) 
        return final_matrix 