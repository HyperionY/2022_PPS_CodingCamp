def solution(x):
    n = x
    n_str = str(n)
    divide_n = 0
    answer = True
    
    for i in n_str: 
        divide_n += int(i)
    
    if n % divide_n != 0: 
        answer = False
    
    return answer