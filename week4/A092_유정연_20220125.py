class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_stack = []
        odd_stack= []
        answer = []
        
        for i in nums:
            if i % 2  == 0:
                even_stack.append(i)
            else:
                odd_stack.append(i)
        
        while even_stack and odd_stack:
            answer.append(even_stack.pop())
            answer.append(odd_stack.pop())

        return answer