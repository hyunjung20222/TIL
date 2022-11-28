"""
[참고]

맨 첫줄 Test case를 입력받을 때는 input()을 사용해도 무방합니다.
그러나 반복문으로 여러줄 입력받는 상황에서는 반드시 sys.stdin.readline()을 사용해야 시간초과가 발생하지 않습니다.

sys.stdin.readline()은 한줄 단위로 입력받기 때문에, 개행문자가 같이 입력 받아집니다.
만약 3을 입력했다면, 3\n 이 저장되기 때문에, 개행문자를 제거해야 합니다.
또한, 변수 타입이 문자열 형태(str)로 저장되기 때문에, 정수로 사용하기 위해서 형변환을 거쳐야 합니다.
"""
# 참고 링크
# https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline

import sys
N = int(input())

for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)