class Solution:
    def dayOfYear(self, date: str) -> int:
        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:])
        answer = 0
        
        if year != 1900 and year % 4 == 0:
            months[2] = 29
        
        answer = sum(months[:month]) + day
        
        return answer