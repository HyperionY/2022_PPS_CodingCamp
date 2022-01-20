class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        stack_fivbil = []
        stack_tenbil = []
        answer = True
        
        for i in bills:
            if i == 5:
                stack_fivbil.append(5)
            elif i == 10:
                if stack_fivbil:
                    stack_fivbil.pop()
                    stack_tenbil.append(10)
                else:
                    answer = False
                    break
            elif i == 20:
                if not stack_fivbil:
                    answer = False
                    break
                else:
                    if stack_fivbil and stack_tenbil:
                        stack_fivbil.pop()
                        stack_tenbil.pop()
                    elif len(stack_fivbil) > 2:
                        for _ in range(3):
                            stack_fivbil.pop()
                    else:
                        answer = False
                        break
        
        return answer
                