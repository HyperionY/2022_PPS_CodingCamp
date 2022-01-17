class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        count = 0
        answer = []
        
        while count < numRows:
            if count > 1:
                n_list = []
                prev_list = answer[count-1]
                
                for i in range(len(prev_list)):
                    if i != 0:
                        n_list.append(prev_list[i] + prev_list[i-1])
                    else:
                        n_list.append(1)
                n_list.append(1)
                answer.append(n_list)
            elif count == 0:
                answer.append([1])
            elif count == 1:
                answer.append([1,1])
            count += 1
        
        return answer