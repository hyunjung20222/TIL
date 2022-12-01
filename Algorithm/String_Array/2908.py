"""
상수는 수를 다른 사람과 다르게 거꾸로 읽는다.
예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다.
따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.
두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.

첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다.
두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.
"""

"""
reverse 는 값을 반환하지 않고 list 를 순서 반대로 만들기만 한다
reversed 는 순서가 반대로 된 객체를 반환한다
"""
# 리스트를 문자열로 만들기 위해선 ''.join(list) 이렇게 작성하면 된다

import sys

A, B = map(int, sys.stdin.readline().split())
reverseA = A % 10 * 100 + A % 100 // 10 * 10 + A // 100
reverseB = B % 10 * 100 + B % 100 // 10 * 10 + B // 100

if reverseA > reverseB:
    print(reverseA)
else:
    print(reverseB)