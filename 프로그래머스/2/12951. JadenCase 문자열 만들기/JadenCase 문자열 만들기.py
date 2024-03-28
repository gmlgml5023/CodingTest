def solution(s):
    return ' '.join([st[0].upper() + st[1:].lower() if len(st) > 0 else '' for st in s.split(" ")])