"""
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.

첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다.
각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다.
S의 길이는 적어도 1이며, 20글자를 넘지 않는다.
"""

import sys
T = int(input())
for n in range(1, T+1):
    R, S = map(str, sys.stdin.readline().split())
    R = int(R)

    ans = ''

    for char in S:
        ans += char * R
    print(ans)