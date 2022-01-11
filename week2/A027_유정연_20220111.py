def solution(number, k):
    answer = ''
    n = -(len(number) - k - 1)
    number_str = number

    for _ in range(len(number) - k):
        top_num = '0'
        top_i = 0
        
        if n > 0: 
            break
        
        if n == 0: 
            c_str = number_str
        else: 
            c_str = number_str[:n]

        for i in range(len(c_str)): 
            if c_str[i] > top_num: 
                top_num = c_str[i]
                top_i = i
                
            if top_num == '9': 
                break

        answer += top_num
        number_str = number_str[top_i+1:]
        n += 1

    return answer