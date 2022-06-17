class Solution:
    def dayOfYear(self, date: str) -> int:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        date_split = date.split('-')
        dd = int(date_split[2])
        mm = int(date_split[1])
        yyyy = int(date_split[0])
        
        days = dd + sum(month_days[:mm-1])
        
        if ((yyyy % 100 == 0 and yyyy % 400 == 0) or (yyyy % 100 != 0 and yyyy % 4 == 0)) and (mm > 2):
            days += 1
        
        return days