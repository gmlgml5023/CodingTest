import sys
N = int(input())

word_list = [sys.stdin.readline().strip() for _ in range(N)]
word_list = list(set(word_list))
word_list.sort(key = lambda x : (len(x), x))

for word in word_list:
    print(word)