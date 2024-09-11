def solution(str1, str2):
    N, M = len(str1), len(str2)

    ss1 = [str1[i:i+2].lower() for i in range(N-1) if str1[i:i+2].isalpha()]
    ss2 = [str2[i:i+2].lower() for i in range(M-1) if str2[i:i+2].isalpha()]

    copy_ss2 = ss2.copy()
    
    len_intersection = 0
    for s in ss1:
        if s in copy_ss2:
            copy_ss2.remove(s)
            len_intersection += 1

    len_union = len(ss1) + len(ss2) - len_intersection

    return int(len_intersection / len_union * 65536) if (len_intersection != 0 or len_union != 0) else 65536