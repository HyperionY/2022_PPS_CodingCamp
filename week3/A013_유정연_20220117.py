class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        stack = []
        answer = []
        for i in nums:
            if not i in stack:
                stack.append(i)
                answer.append(i)
            else:
                answer.remove(i)
        
        return answer[0]