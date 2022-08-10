def solution(a, b):
    
    weekday = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    total = sum(days[:a-1]) + b
    
    return weekday[total % 7]