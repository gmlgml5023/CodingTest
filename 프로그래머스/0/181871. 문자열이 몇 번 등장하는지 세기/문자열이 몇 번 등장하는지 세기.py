def solution(myString, pat):
    return len([myString[i:i+len(pat)] for i in range(len(myString)) if myString[i:i+len(pat)] == pat])