"""
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

input 예시
5 테스트 케이스
1 1
2 3
3 4
9 8
5 2
"""

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(A + B)