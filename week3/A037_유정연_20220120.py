class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        n = left
        answer = []
        
        while n <= right:
            divd_num_list = list(map(int, str(n)))
            answer.append(n)
            
            for i in divd_num_list:
                if i == 0 or n % i != 0:
                    answer.pop()
                    break
            n += 1
        
        return answer