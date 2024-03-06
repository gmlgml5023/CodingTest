def solution(myString):
    answer = 'abcdefghijk'
    for s in myString:
        if s in answer:
            myString = myString.replace(s, 'l')
    return myString