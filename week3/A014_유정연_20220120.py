class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        stack = []
        answer = []
        
        for i in nums: 
            if not stack:
                stack.append(i)
            else:
                if (stack[-1]+1) == i:
                    stack.append(i)
                else:
                    if stack[0] == stack[-1]:
                        answer.append(str(stack.pop()))
                    else:
                        answer.append(str(stack[0]) + "->" + str(stack[-1]))
                        stack.clear()
                    stack.append(i)
        
        if stack:
            if stack[0] == stack[-1]:
                answer.append(str(stack.pop()))
            else:
                answer.append(str(stack[0]) + "->" + str(stack[-1]))
        
        return answer