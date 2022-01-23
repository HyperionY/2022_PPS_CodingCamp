def solution(board, moves):
    answer = 0
    w_size = len(board[0])
    m = [[] for i in range(w_size)]
    stack = []
    board.reverse()
    
    for w in board:
        for i in range(0, w_size):
            if not w[i] == 0:
                m[i].append(w[i])
    
    for i in moves:
        n = i - 1
        if m[n]:
            item = m[n].pop()
            if stack and item == stack[-1]:
                stack.pop()
                answer += 2
            else:
                stack.append(item)
            
    return answer