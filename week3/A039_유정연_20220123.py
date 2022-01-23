class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        answer = False
        if num ** 0.5 == int(num ** 0.5):
            answer =True
        
        return answer