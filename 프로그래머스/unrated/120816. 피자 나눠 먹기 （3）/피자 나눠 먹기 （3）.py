def solution(slice, n):
    return n//slice if n % slice == 0 else n//slice + 1

def sloution2(slice, n):
    d, m = divmod(n, slice)
    return d + int(m != 0)