"""
BackJoon 설명 참고

곱셈 과정에서 들어갈 수를 구하는 문제
첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.
"""

import sys
sys.stdin = open('input.txt', 'r')
# 일단 숫자를 받는다
firstNum = int(input())
secNum = int(input())

# 두번째 숫자를 숫자 리스트로 만든다
secNumArr = list(map(int, str(secNum)))

# 각자 곱한 것을 출력한다
# 세 자리 자연수라 했으므로 인덱스가 2까지 있고, 끝에서부터 계산
print(firstNum * secNumArr[2])
print(firstNum * secNumArr[1])
print(firstNum * secNumArr[0])
print(firstNum * secNum)
