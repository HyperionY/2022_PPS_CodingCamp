class Solution:
    def addDigits(self, num: int) -> int:
        answer = num
        
        while answer > 9:
            list_nums = list(map(int, str(answer)))
            answer = sum(list_nums)
        
        return answer