class Solution:
    def addBinary(self, a: str, b: str) -> str:
        str1 = '0b' + a
        str2 = '0b' + b
        n1 = int(str1, 2)
        n2 = int(str2, 2)
        
        answer = bin(n1 + n2)
        
        return answer[2:]