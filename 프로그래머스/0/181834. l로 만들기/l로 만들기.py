def solution(myString):
    ch = 'abcdefghijk'
    return ''.join(['l' if s in ch else s for s in myString])

def solution2(myString):    
    return ''.join([s if s > 'l' else 'l' for s in myString])