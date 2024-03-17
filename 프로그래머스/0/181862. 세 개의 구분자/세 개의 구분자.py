def solution(myStr):
    result = [s for s in myStr.replace('a','b').replace('b', 'c').split('c') if len(s)>0]
    return ["EMPTY"] if len(result)==0 else result