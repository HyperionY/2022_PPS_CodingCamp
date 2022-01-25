class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        list_students = sorted(heights)
        answer = 0
        
        for i in range(0, len(heights)):
            if heights[i] != list_students[i]:
                answer += 1
        
        return answer
            