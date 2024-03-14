def solution(myString, pat):
    if myString.count(pat) == 1:
        return myString.split(pat)[0]+pat
    else:
        return myString[:[i for i,a in enumerate(myString) if a == pat][-1]+1]
