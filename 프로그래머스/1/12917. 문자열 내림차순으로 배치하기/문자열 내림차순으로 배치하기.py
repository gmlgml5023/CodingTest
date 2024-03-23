def solution(s):
    return ''.join(sorted([ss for ss in s if ss.islower()], reverse=True)) + ''.join(sorted([ss for ss in s if ss.isupper()], reverse=True))