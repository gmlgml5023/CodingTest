def solution(s):
    return True if ((len(s)==4) or (len(s)==6)) and (s.isnumeric() is True) else False