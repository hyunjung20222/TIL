"""
첫째 줄에는 영수증에 적힌 총 금액 X 가 주어진다.
둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N 이 주어진다.
이후 N 개의 줄에는 각 물건의 가격 a 와 개수 b 가 공백을 사이에 두고 주어진다.

구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 Yes 를 출력한다.
일치하지 않는다면 No 를 출력한다.
"""

import sys
sys.stdin = open('input.txt', 'r')

total = int(input())
num = int(input())
cal = 0

for i in range(num):
    a, b = map(int, input().split())
    cal += a * b

if cal == total:
    print('Yes')
else:
    print('No')