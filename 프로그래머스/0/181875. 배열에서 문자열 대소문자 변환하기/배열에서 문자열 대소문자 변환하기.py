def solution(strArr):
    return [a.lower() if i%2==0 else a.upper() for i,a in enumerate(strArr)]