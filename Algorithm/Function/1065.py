"""
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
"""

# 구현 방법 1: 틀렸습니다!
# 이유 찾아야 한다..
"""
N = int(input())
# 자리수 숫자 리스트
numlist = []

for num in str(N):
    numlist.append(int(num))


def getnum(n=[]):
    cnt = 99
    for i in range(1, n[0]):
        for k in range(-i, 10 - i):
            if 0 <= i + k * 2 < 10:
                cnt += 1
    for j in range(-n[0], 10 - n[0]):
        if 0 <= n[0] + j <= n[1] and 0 <= n[0] + j * 2 <= n[2]:
            cnt += 1
    return cnt

if N < 100:
    print(N)
elif 100 <= N < 1000:
    ans = getnum(numlist)
    print(ans)
else:
    newlist = [9, 9, 9]
    ans = getnum(newlist)
    print(ans)
"""

# 구현 방법 2
N = int(input())
cnt = 0

for i in range(1, N+1):
    if i < 100:
        cnt += 1
    elif i < 1000:
        if (i % 10 - i//10%10 == i//10 % 10 - i//100):
            cnt += 1
print(cnt)