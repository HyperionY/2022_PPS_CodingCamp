def solution(array, commands):
    answer = []
    
    for i in commands:
        slice_arr = array[(int(i[0])-1):(int(i[1]))]
        slice_arr.sort()
        answer.append(slice_arr[int(i[2])-1])
        
    return answer