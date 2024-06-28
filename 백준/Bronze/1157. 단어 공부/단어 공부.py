word = input().strip().lower()
cnt = [word.count(l) for l in list(set(word))]
if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(list(set(word))[cnt.index(max(cnt))].upper())