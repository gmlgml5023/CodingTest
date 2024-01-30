def solution(polynomial):
    xs = 0
    num = 0

    for p in polynomial.split(' + '):
        if 'x' in p:
            if p =='x':
                xs += 1
            else:
                xs += int(p[:-1])
        elif p.isdigit():
            num += int(p)

    if (xs!=0)&(num==0):
        answer = f'{xs}x' if xs!=1 else 'x'
    elif (xs==0)&(num!=0):
        answer = str(num)
    elif (xs!=0)&(num!=0):
        answer = f'{xs}x + {num}' if xs!=1 else f'x + {str(num)}'
        
    return answer