class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_n = "".join(map(str, digits))
        int_n = int(str_n) + 1
        answer = list(map(int, str(int_n)))
        
        return answer