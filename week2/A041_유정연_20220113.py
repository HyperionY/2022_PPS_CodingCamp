def solution(s): 
    s = s.title()
    
    for i in range(len(s)):
        if i != 0 and s[i-1] != " ":
            s = s[:i] + s[i].lower() + s[i+1:]
            
    return s