class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        
        for i in ops:
            if i == "C":
                stack.pop()
            elif i == "D":
                buff = stack[-1] * 2
                stack.append(buff)
            elif i == "+":
                buff = stack[-1] + stack[-2]
                stack.append(buff)
            else:
                stack.append(int(i))
        
        return sum(stack)
                