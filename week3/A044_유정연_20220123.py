class Solution:
    def checkRecord(self, s: str) -> bool:
        answer =True
        stack = []

        for i in range(0, len(s)):
            if s[i] == 'A':
                stack.append(i)
            elif s[i] == 'L' and len(s[i:]) > 2:
                if s[i+1] == 'L' and s[i+2] == 'L':
                    answer = False
                    break

            if len(stack) > 1:
                answer = False
                break
        
        return answer