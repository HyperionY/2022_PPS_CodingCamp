def solution(a, b):
    answer = ''
    season = [4, 0, 1, 4, 6, 2, 4, 0, 3, 5, 1, 3]
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    
    currentSeason = a - 1
    currentDay = ((season[currentSeason] + (b % 7)) % 7) - 1
    
    if currentDay == -1:
        currentDay = 6
    
    answer = days[currentDay]
    
    return answer