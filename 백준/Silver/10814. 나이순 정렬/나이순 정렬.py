import sys

# 모든 입력을 한 번에 읽기
input = sys.stdin.read
data = input().strip().split('\n')

N = int(data[0])  # 첫 번째 줄에서 회원 수 가져오기
members = []

# 나이와 이름을 튜플 형태로 리스트에 저장
for i in range(1, N + 1):
    age, name = data[i].split()
    members.append((int(age), name))  # 나이는 int로 변환하여 저장

# 나이를 기준으로 정렬 (안정 정렬)
members.sort(key=lambda x: x[0])

# 정렬된 회원들 출력
for age, name in members:
    print(age, name)
