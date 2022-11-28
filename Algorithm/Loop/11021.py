"""
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

출력 예시
Case #1: 2
"""

import sys
T = int(input())

for i in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    print("Case #" + str(i) + ":", A + B)