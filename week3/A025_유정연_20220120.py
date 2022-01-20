class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        answer = True
        
        while n != 1:
            if n == 0 or n % 4 != 0:
                answer = False
                break
            n = n/4
        
        return answer